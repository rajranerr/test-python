# Readline() method: The readline() method read a single line from the file. If we want to read multiple lines, we can use a loop.
#  Ex:
f = open('example.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# Readlines() method: The readlines() method reads all the lines of the file and return them as a list of strings.
# Ex:
f =open('example.txt', 'r')
line = f.readlines()
print(line)
f.close()

# Writelines() method: The writeline() method in python write a squence of string to a file. The sequence can be any iterable object, such as a list or a tuple.
# Ex:
f = open('example.txt', 'w')
lines = ['My name is Raj Rane\n', 'My father is a farmer\n', 'Hunter 350 and interseptor 650 are my favorite bikes\n']
f.writelines(lines)
f.close()

# readable(): Returns a boolean (True/False) indicating whether the file can be extracted from (e.g., if it was opened in 'r' or 'r+' mode).

# writable(): Returns a boolean indicating whether the file can accept incoming data modifications (e.g., if opened in 'w' or 'a' mode).

# Reading Specific Parts of a File:Sometimes, we may only need to read a specific part of a file, such as the first few bytes, a specific line, or a range of lines.
# Ex:
# file = open("example.txt","r")
# content = file.read(10)
# print(content)
# file.close()

# Reading CSV Files:CSV (Comma-Separated Values) is widely used for storing tabular data. Python’s csv module helps parse CSV easily. Here, instead of needing an external file, we’ll simulate one using io.StringIO
# Ex: 
import csv
import io

# Create a CSV sample in memory
csv_data = """Year,Industry,value
2014,Manufacturing,769200
2014,Manufacturing,48200
2014,Menufacturing,16
"""
csvfile = io.StringIO(csv_data)
csvreader = csv.reader(csvfile)
for row in csvreader:
    print(row)