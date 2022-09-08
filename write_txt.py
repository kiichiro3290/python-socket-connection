import sys
import datetime

def main(link_num, output_file_name):
  packet_num = 0
  current_date = str(datetime.datetime.now().strftime('%Y_%m%d_%H%M%S'))
  with open(f'../data/{output_file_name}', 'w') as f:
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
            l = line.rstrip() + "," + str(datetime.datetime.now().strftime('%Y_%m%d_%H%M%S') + "\n")
            f.write(l)
            if current_date != str(datetime.datetime.now().strftime('%Y_%m%d_%H%M%S')):
                msg = current_date + ': link' + str(link_num) + ':' + str(packet_num) + 'Hz'
                print(msg)
                current_date = str(datetime.datetime.now().strftime('%Y_%m%d_%H%M%S'))
                packet_num = 0
            packet_num += 1
  return

if __name__ == '__main__':
  args = sys.argv
  link_num = args[1]
  output_file_name = args[2]
  main(link_num, output_file_name)
