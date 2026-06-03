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