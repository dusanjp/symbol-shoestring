https://github.com/symbol/product/tree/dev/tools/shoestring/shoestring/wizard

上記にある symbol-shoestringの`product/tree/dev/tools/shoestring/shoestring/wizard`以下にある

setup_file_generator.py

ShoestringOperation.py

を、入れ替えて使用する。

2025_06_28　変更内容：

1.wizardの setupﾒﾆｭｰで、新規で nodeﾃﾞｨﾚｸﾄﾘが作成され、nodeﾃﾞｨﾚｸﾄﾘの中に node本体が収納される

2.wizardの その他の ﾒﾆｭｰでも、--directory nodeを指定した動作を行う。

3.又、wizard上のsetup実行時に、metadataの設定が無くても、内容が空'{}'のrest_overrides.jsonが生成される

4.wizardの upgrade命令で、必ず --rest-overrides shoestring/rest_overrides.jsonが適用される

2025_07_01　変更内容：
5.wizardでの renew-certificatesﾒﾆｭｰで、--retain-node-keyを適用しました。



https://github.com/symbol/product/tree/dev/tools/shoestring/shoestring/wizard

Use the setup_file_generator.py and ShoestringOperation.py under product/tree/dev/tools/shoestring/shoestring/wizard in the symbol-shoestring above.

2025_06_28 Changes:

1.A new node directory is created in the wizard setup menu, and the node itself is stored in the node directory.

2.Other wizard menus also perform the operation specified by --directory node.

3.When running setup on the wizard,Even if there is no metadata setting, rest_overrides.json with an empty '{}' content is generated.

4.The wizard upgrade command always applies --rest-overrides shoestring/rest_overrides.json.

2025_07_01 Changes:

5.In the renew-certificates menu in the wizard, I applied --retain-node-key.
