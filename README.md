# 使い方
## esp32に接続しているPCをクライアントにする
-  `~/esp/esp-idf/esp32-csi-tool/python_utils/` ディレクトリに `client.py` を入れる
- `idf.py -p [PORT] monitor | python ../python_utils/client.py` で実行


## データを集めたいPC上でサーバーを立ち上げる
- データを受信する方のPCに　`server.py` をインストールする
- `server.py` が入っているディレクトリで `python server.py` 
- サーバーが起動している状態で，クライアントのスクリプトを実行するとデータが送られてくる


## エラー

### IPアドレスを指定しているのにソケット通信できない
- クライアントのPCとサーバーのPCが同じネットワークになくてエラーが出てました
