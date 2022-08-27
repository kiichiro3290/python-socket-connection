# client.py
import datetime
import sys
import socket

ip_address = 'サーバー側のIPアドレス'
port = 7010
buffer_size = 4092

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # request connection to server
    s.connect((ip_address, port))
    # Append the first line with ",timestamp"
    while True:
        try:
            line = sys.stdin.readline()
        except:
            continue
        if "CSI_DATA" in line:
            l = line.rstrip() + ",timestamp" + "\n"
            # send the data to server
            s.sendall(l.encode())
            break
    # Append subsequent lines with the current timestamp
    while True:
        try:
            line = sys.stdin.readline()
        except:
            continue
        if "CSI_DATA" in line:
            l = line.rstrip() + "," + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S') + "\n")
            # send the data
            s.sendall(l.encode())
