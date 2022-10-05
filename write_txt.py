import sys
import datetime

def main(link_num, output_file_name):
  packet_num = 0
  current_date = str(datetime.datetime.now().strftime('%Y_%m%d_%H%M%S'))
  with open(f'./data/{output_file_name}_link{link_num}', 'w') as f:
    while True:
        line = sys.stdin.readline()

        if "CSI_DATA" in line:
            l = line.rstrip() + ",timestamp" + "\n"
            f.write(l)
            break
    # Append subsequent lines with the current timestamp
    while True:
        line = sys.stdin.readline()

        if "CSI_DATA" in line:
            # ファイルにデータを書き込む
            l = line.rstrip() + "," + str(datetime.datetime.now().strftime('%Y_%m%d_%H%M%S') + "\n")
            f.write(l)
            # 毎秒のパケット数をターミナルに表示(ファイルにはデータを出力する)
            if current_date != str(datetime.datetime.now().strftime('%Y_%m%d_%H%M%S')):
                msg = current_date + ': link' + str(link_num) + ':' + str(packet_num) + 'Hz'
                print(msg)
                current_date = str(datetime.datetime.now().strftime('%Y_%m%d_%H%M%S'))
                packet_num = 0
            packet_num += 1
  return

# コマンドライン引数として，リンクの番号とデータの出力ファイルを受け取る
if __name__ == '__main__':
  args = sys.argv
  link_num = args[1]
  output_file_name = args[2]
  main(link_num, output_file_name)
