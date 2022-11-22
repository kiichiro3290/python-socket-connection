from os import link
import sys
import socket
import datetime
from contextlib import closing

# CSIデータを取得して，毎秒のパケット数を計算して，パケットrateの情報をサーバへ送信する
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
            # メタデータにタイムスタンプとリンク番号を追加する
            l = line.rstrip() + ",timestamp" + ",link_num" + "\n"
            # send the data to server
            sock.sendall(l.encode())
            break

    # パケットrate計測のための準備
    packet_num = 0
    current_date = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

    # Append subsequent lines with the current timestamp
    while True:
        line = sys.stdin.readline()

        if "CSI_DATA" in line:
            # タイムスタンプとリンク数を追加
            l = line.rstrip() + "," + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S') + "," + str(link_num) + "\n")
            
            # packet rate をサーバへ送信
            if current_date != str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')):
                msg = current_date + ': link' + str(link_num) + ':' + str(packet_num) + 'Hz'
                sock.sendall(msg.encode('utf-8'))
                current_date = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
                packet_num = 0

            packet_num += 1

if __name__ == '__main__':
  args = sys.argv
  link_num = args[1]
  main(link_num)
