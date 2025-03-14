#server.py
import socket
import datetime

IP_ADDR = 'サーバ側のIPアドレス'
PORT = 8890 # port は 0 ~ 65535 まである．このうち49151までは何かしらのアプリケーションが既に登録されてある．特に，0番～1023番はよく使われるアプリケーション
BUF_SIZE = 4092

# テキストファイルで出力するサーバ
def main():
    # create the socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # assign the IP Adress and the Port number
        s.bind((IP_ADDR, PORT))

        datetime_str = str(datetime.datetime.now().strftime('%Y%m%d%H%M'))

        # csv で出力すると１つの列にデータが詰まるので良くない
        while True:
            # receive the data
            raw_data, cli_addr = s.recvfrom(BUF_SIZE)
            data = raw_data.decode('utf-8')
            print(data)

            # 機械学習パートへ流す

if __name__ == '__main__':
    main()