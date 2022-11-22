import sys
import socket
import datetime
from contextlib import closing

def main(link_num):
  host = 'サーバー側のIPアドレス'
  port = 50000
  bufsize = 4096

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  with closing(sock):
    sock.connect((host, port))
    while True:
        line = sys.stdin.readline()

        if "CSI_DATA" in line:
            l = line.rstrip() + ",timestamp" + "\n"
            # send the data to server
            sock.sendall(l.encode())
            break
    # Append subsequent lines with the current timestamp
    while True:
        line = sys.stdin.readline()

        if "CSI_DATA" in line:
            l = line.rstrip() + "," + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S') + "\n")
            # データを送信する
            sock.sendall(l.encode('utf-8'))
  return

if __name__ == '__main__':
  args = sys.argv
  link_num = args[1]
  main(link_num)