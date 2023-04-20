# client.py
import datetime
import sys
import socket

IP_ADDR = 'サーバー側のIPアドレス'
PORT = 8890
BUF_SIZE = 4092

# テキストファイルで出力するクライアント
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # サーバーに接続を要求する
        s.connect((IP_ADDR, PORT))
        # Append the first line with ",timestamp"
        while True:
            line = sys.stdin.readline()

            if "CSI_DATA" in line:
                l = line.rstrip() + ",timestamp" + '\n'
                # send the data to server
                s.sendall(l.encode('utf-8'))
                break
        # Append subsequent lines with the current timestamp
        while True:
            line = sys.stdin.readline()

            if "CSI_DATA" in line:
                l = line.rstrip() + "," + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '\n')
                # データを送信する
                s.sendall(l.encode('utf-8'))

if __name__ == '__main__':
    main()
