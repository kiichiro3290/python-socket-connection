# client.py
import sys
import socket
import time

ip_address = 'サーバー側のIPアドレス'
port = 7010
buffer_size = 4092

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバーに接続を要求する
    s.connect((ip_address, port))
    # Append the first line with ",timestamp"
    while True:
        line = sys.stdin.readline()

        if "CSI_DATA" in line:
            l = line.rstrip()
            # send the data to server
            s.sendall(l.encode())
            break
    # Append subsequent lines with the current timestamp
    while True:
        line = sys.stdin.readline()

        if "CSI_DATA" in line:
            l = line.rstrip() + "," + str(time.time())
            # データを送信する
            s.sendall(l.encode())