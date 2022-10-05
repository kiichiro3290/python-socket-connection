# How to use
## prepare
### esp-idf
 - [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/release-v4.3/esp32/get-started/index.html)
### esp-csi-tool
 - [ESP-CSI-tool](https://github.com/StevenMHernandez/ESP32-CSI-Tool)

## what is the socket communication
 - [TCP/IP](https://www.itmanage.co.jp/column/tcp-ip-protocol/)
 - [python socket-communication](https://office54.net/python/app/python-data-socket)

## system configration
![esp32csisystem](https://user-images.githubusercontent.com/80093134/182512286-9df52333-cf04-46b4-b0b1-8b22308eff1b.png)

## esp32に接続しているPC(Odyssey)をクライアントにする
-  `~/esp/esp-idf/esp32-csi-tool/python_utils/` ディレクトリに `client.py` を入れる
- `idf.py -p [PORT] monitor | python ../python_utils/client.py` で実行


## データを集めたいPC上でサーバーを立ち上げる
- データを受信する方のPCに　`server.py` をインストールする
- `server.py` が入っているディレクトリで `python server.py` 
- サーバーが起動している状態で，クライアントのスクリプトを実行するとデータが送られてくる

## write the CSI data to csv file
 - `python writeCsv.py`


## エラー

### IPアドレスを指定しているのにソケット通信できない
- クライアントのPCとサーバーのPCが同じネットワークになくてエラーが出てました

# ファイルの説明

### write_txt.py
 - ESP32 から送られてきたデータをテキストファイルとして保存するためのスクリプト
 - ESP32 から送られてきたデータをサーバに送信するために， `write_txt_server.py` と `write_txt_client.py` を用いる
 
### write_csv.py
 - ESP32 から送られてきたデータを csv ファイルとして保存するためのスクリプト
 - csv ファイルとして保存すると，1行に複数のデータが入る場合があったためテキストファイルとして保存して csv ファイルに変換するようにした

### show_packet_number.py
 - 毎秒のパケット数を表示するだけのスクリプト
 
### select_client.py, select_server.py
 - 1台のサーバ PC に対して，　複数のクライアント PC からデータを送受信するためのスクリプト

### convert_txt_to_csv.py
 - txt ファイルから csv ファイルへ変換する
