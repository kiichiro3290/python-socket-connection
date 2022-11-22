import sys
import csv

# テキストファイルをCSVファイルに変換するスクリプト
def main(input_file, output_file):
    f1 = open(input_file)
    lines = f1.readlines()
    with open(output_file, "w") as f:
        for l in lines:
            row=list(l.split(','))
            writer=csv.writer(f)
            writer.writerow(row)

if __name__ == '__main__':
    args = sys.argv

    print(args[0])
    print("inputfile:" + args[1])
    print("outputfie:" + args[2])

    main(args[1], args[2])
