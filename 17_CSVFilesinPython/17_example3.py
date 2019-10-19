import csv

path = ".\\17_CSVFilesinPython\\data\\google_stock_data.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) # The first line is the header
data = [row for row in reader] # Read the remaining data

print(header)
print(data[0])