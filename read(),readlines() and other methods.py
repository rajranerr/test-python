# Readline() method: The readline() method read a single line from the file. If we want to read multiple lines, we can use a loop.
#  Ex:
f = open('example.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)