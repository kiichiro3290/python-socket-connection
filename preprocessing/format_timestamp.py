import sys
import csv

args = sys.argv

print(args[0])
print("inputfile:" + args[1])
print("outputfie:" + args[2])
with open(args[1], "r") as f1:
    reader = csv.reader(f1)
    with open(args[2], "w") as f2:
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