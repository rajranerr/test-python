# Opening a File: Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which The file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.

# Example:
# Ex 1: Writing to a file(w): Use the "w" mode to open a file for writing.
f = open('example.txt','w')
f.write('Hello i am raj\n')
f.write('I am from haidarpur')
f.close()
# Ex 2: Reading a File(r): Use the "r" mode to extract data. 
f = open('example.txt','r')
# print(f)
text = f.read()
print(text)
f.close()

# Ex 3: Appending a File (a): Use the "a" mode to add new data safely to the end of an existing file without deleting its current contents.

f = open('example.txt','a')
f.write("\n My favorite bike is Interseptor 650")
f.close()

# Ex 4:
# Read and write("r+"): Opens the file with the pointer placed at the beginning.
f = open('example.txt','r+')
f.write("Hello world!\n")
f.close()

# Ex 5:
# Binary Mode("b"): Used for non-text formats like images (e.g., "rb", "wb").
f = open('example.txt','rb')
text = f.read()
print(text)
f.close()

# Ex 6:
# Checking File Properties: Once the file is open, we can check some of its properties:
f = open('example.txt','r')
print('filename:', f.name)
print('Mode:', f.mode)
print('Is closed?', f.closed)

f.close()
print('Is Closed?', f.closed)

# Ex 7:
# Handling Excceptions When Closing a File:It's important to handle exceptions to ensure that files are closed properly, even if an error occurs during file operations. Here, the finally block ensures the file is closed even if an error occurs.

try:
    file = open('example.txt','r')
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("Error:", e)
finally:
    file.close()