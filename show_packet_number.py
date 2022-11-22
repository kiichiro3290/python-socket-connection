import sys
import time
import datetime

# CSIデータを取得して，パケット数を表示する,ファイル出力はしない
def main():
    while True:
        line = sys.stdin.readline()

        if "CSI_DATA" in line:
            l = line.rstrip()
            print(line.rstrip() + ",timestamp")
            break

    #
    # Append subsequent lines with the current timestamp
    #

    packet_num = 0
    current_date = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))


    while True:
        line = sys.stdin.readline()

        if "CSI_DATA" in line:
            if current_date != str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')):
                print(current_date + ':' + str(packet_num) + 'Hz')
                current_date = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
                packet_num = 0
            packet_num += 1

if __name__ == '__main__':
    main()