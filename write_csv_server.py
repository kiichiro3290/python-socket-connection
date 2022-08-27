#server.py
import socket
import csv
import datetime

ip_address = 'サーバー側のIPアドレス'
port = 7010 # port は 0 ~ 65535 まである．このうち49151までは何かしらのアプリケーションが既に登録されてある．特に，0番～1023番はよく使われるアプリケーション
buffer_size = 4092

def main():
    # create the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # assing the IP Adress and the Port number
        s.bind((ip_address, port))
        # creating socket
        s.listen(5)
        datetime_str = str(datetime.datetime.now().strftime('%Y%m%d%H%M'))
        # csv で出力
        with open(f'../data/{datetime_str}_link1.csv', 'w') as f:
            writer=csv.writer(f)
            # wait for client sending the socket
            try:
                while True:
                    # 要求があれば接続の確立とアドレス、アドレスを代入
                    # establish client/server communication
                    conn, addr = s.accept()
                    while True:
                        # receive the data
                        data = conn.recv(buffer_size)
                        # write csv file
                        csvData = list(data.decode().split(','))
                        writer.writerow(csvData)

                        # use for debugging
                        print(data.decode())
            finally:
                s.close()
                
if __name__ == '__main__':
    main()