import sys
import socket
import datetime
from contextlib import closing

# CSIデータを取得して，タイプスタンプとリンク番号のcolumnを追加して，サーバへデータを通信する
def select_client(link_num):
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
            l = line.rstrip() + ",timestamp" + ",link_num"
            # send the data to server
            sock.sendall(l.encode())
            break

    # Append subsequent lines with the current timestamp
    while True:
        line = sys.stdin.readline()

        if "CSI_DATA" in line:
            # タイムスタンプとリンク番号を追加
            l = line.rstrip() + "," + str(datetime.datetime.now().strftime('%m%d%H%M%S') + "," + str(link_num) + "\n")
            
            # server にデータを送信
            msg = l.encode('utf-8')
            sock.sendall(msg)
  return

if __name__ == '__main__':
  args = sys.argv

  # リストの長さで引数の個数を判別
  if len(args) == 2:
    # 実行
    select_client(args[1])
  else:
    print('Usage: python3 select_client.py [LINK_NUM]')