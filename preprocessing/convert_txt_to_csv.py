import sys
import csv

args = sys.argv

print(args[0])
print("inputfile:" + args[1])
print("outputfie:" + args[2])

f1 = open(args[1])
lines = f1.readlines()
with open(args[2], "w") as f:
    for l in lines:
        row=list(l.split(','))
        writer=csv.writer(f)
        writer.writerow(row)

