# client.py
import datetime
import sys
import socket

ip_address = 'サーバー側のIPアドレス'
port = 7010
buffer_size = 4092

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # サーバーに接続を要求する
        s.connect((ip_address, port))
        # Append the first line with ",timestamp"
        while True:
            line = sys.stdin.readline()

            if "CSI_DATA" in line:
                l = line.rstrip() + ",timestamp"
                # send the data to server
                s.sendall(l.encode())
                break
        # Append subsequent lines with the current timestamp
        while True:
            line = sys.stdin.readline()

            if "CSI_DATA" in line:
                l = line.rstrip() + "," + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
                # データを送信する
                s.sendall(l.encode('utf-8'))

if __name__ == '__main__':
    main()