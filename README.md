https://github.com/symbol/product/tree/dev/tools/shoestring/shoestring/wizard

ここにある
setup_file_generator.py
ShoestringOperation.py
を、入れ替えて使用する。

2025_06_28
変更内容：
wizardの setupﾒﾆｭｰで、新規で nodeﾃﾞｨﾚｸﾄﾘが作成され、nodeﾃﾞｨﾚｸﾄﾘの中に node本体が収納される
又、metadataの設定が無くても、内容が空'{}'のrest_overrides.jsonが生成される

wizardの upgrade命令で、必ず --rest-overrides shoestring/rest_overrides.jsonが適用される
