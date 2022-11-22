import sys
import csv

# CSVファイルに出力した時に，タイムスタンプのズレを修正するスクリプト
def main(input_file, output_file):
    with open(input_file, "r") as f1:
        reader = csv.reader(f1)
        with open(output_file, "w") as f2:
            for row in reader:
                row_timestamp = row[-1]
                if 'timestamp' in row_timestamp:
                    writer=csv.writer(f2)
                    writer.writerow(row)
                    continue
                new_timestamp = row_timestamp[10:]
                row.pop(-1)
                row.append(new_timestamp)
                writer=csv.writer(f2)
                writer.writerow(row)

if __name__ == '__main__':
    args = sys.argv
    main(args[1], args[2])