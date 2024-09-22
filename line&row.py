import csv
import pandas
import statistics
csvfile = open("myfile3.csv", "r",newline = '')
csvreader = csv.reader(csvfile)
header = next(csvreader,None)
print("Header:", header)
#using line and row
row = next(csvreader, None)
line = csvfile.readline()
print(line, "readline1")
print(line[0])
print(line[1])
print("Row 1:")
print(row[0])  # Access the first column
print(row[1])
