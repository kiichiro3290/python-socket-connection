# 使い方
## esp32に接続しているPCをクライアントにする
-  `~/esp/esp-idf/esp32-csi-tool/python_utils/` ディレクトリに `client.py` を入れる
- `idf.py -p [PORT] monitor | python ../python_utils/client.py` で実行

## データを集めたいPC上でサーバーを立ち上げる
- `server.py` が入っているディレクトリで `python server.py` 
