import socket
import select
import datetime

def main():
  host = 'サーバー側のIPアドレス'
  port = 50000
  backlog = 10
  bufsize = 4096

  server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  readfds = set([server_sock])
  try:
    server_sock.bind((host, port))
    server_sock.listen(backlog)

    datetime_str = str(datetime.datetime.now().strftime('%Y%m%d%H%M'))
    with open(f'../data/{datetime_str}.txt', 'w') as f:
      while True:
        rready, wready, xready = select.select(readfds, [], [])
        for sock in rready:
          if sock is server_sock:
            conn, address = server_sock.accept()
            readfds.add(conn)
          else:
            msg = sock.recv(bufsize)
            if len(msg) == 0:
              sock.close()
              readfds.remove(sock)
            else:
              print(msg.decode())
              # ファイルを保存する
              f.write(msg.decode())

  finally:
    for sock in readfds:
      sock.close()
  return

if __name__ == '__main__':
  main()
