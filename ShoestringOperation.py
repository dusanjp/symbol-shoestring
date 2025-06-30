from enum import Enum
from pathlib import Path


class ShoestringOperation(Enum):
	"""Supported shoestring operations."""

	SETUP = 1
	UPGRADE = 2
	RESET_DATA = 3
	RENEW_CERTIFICATES = 4
	RENEW_VOTING_KEYS = 5
	IMPORT_BOOTSTRAP = 6


def requires_ca_key_path(operation):
	"""Determines if CA key is required for completing operation."""

	return operation in (ShoestringOperation.SETUP, ShoestringOperation.RENEW_CERTIFICATES)


def build_shoestring_command(
	operation,
	destination_directory,
	shoestring_directory,
	ca_pem_path,
	package,
	has_custom_rest_overrides=False
):  # pylint: disable=too-many-arguments,too-many-positional-arguments
	"""Builds shoestring command arguments."""

	command_name = None
	if ShoestringOperation.SETUP == operation:
		command_name = 'setup'
	elif ShoestringOperation.UPGRADE == operation:
		command_name = 'upgrade'
	elif ShoestringOperation.RESET_DATA == operation:
		command_name = 'reset-data'
	elif ShoestringOperation.RENEW_CERTIFICATES == operation:
		command_name = 'renew-certificates'
	elif ShoestringOperation.RENEW_VOTING_KEYS == operation:
		command_name = 'renew-voting-keys'

	shoestring_args = [
		command_name,
		'--config', str(Path(shoestring_directory) / 'shoestring.ini'),
		'--directory', str(Path(destination_directory) / 'node')
	]

	if requires_ca_key_path(operation):
		shoestring_args.extend(['--ca-key-path', str(ca_pem_path)])

	if operation in (ShoestringOperation.SETUP, ShoestringOperation.UPGRADE):
		shoestring_args.extend([
			'--overrides', str(Path(shoestring_directory) / 'overrides.ini'),
            '--rest-overrides', str(Path(shoestring_directory) / 'rest_overrides.json'),
			'--package', package
		])

	if ShoestringOperation.SETUP == operation:
		shoestring_args.extend(['--security', 'insecure'])

	if operation == ShoestringOperation.SETUP:
		Path(destination_directory, "node").mkdir(parents=True, exist_ok=True)

	if ShoestringOperation.RENEW_CERTIFICATES == operation:
		shoestring_args.extend(['--retain-node-key'])

	return shoestring_args
