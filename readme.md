# vCard-UTF8-Encord-Fixer
vCardでUTF-8でエンコードされていない文字列をエンコードするスクリプトです。
「=E3=81=9F=E3=81=8F=E3=81=82=E3=82=93」とかってなってるのを「たくあん」というふうに置き換えます。
<br>らくらくスマートフォンからiPhoneに連絡先を移動しようとしたらこいつのせいで文字化けして移行できない！！！！とかいう仕様だったので作りました。
<br>Google Contacts使ってエクスポートしても無理だったのあれなんでだろ
<br>ちなみにvCard2.1から3.0にアップデートします。多分。わからん。

## 使い方
1. このリポジトリをクローン
2. クローンしたディレクトリに移動
3. `python3 vcard_utf8_encord_fix.py [FILE_PATH]`を実行
4. なななななななんと！！！！！綺麗な連絡先ファイルができる！！！！

## 注意
連絡先という結構重要なデータを扱うので、自己責任でお願いします。

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

### Permissions
- **Commercial use**: You can use this project for commercial purposes.
- **Modification**: You can modify the code as you wish.
- **Distribution**: You can share this project freely.
- **Private use**: You can use this project in private.

### Limitations
- **Liability**: The author is not responsible for any damages caused by using this project.
- **Warranty**: This project is provided "as-is," without any warranty of any kind.