# seek() and tell() functions:  the seek() and tell() functions are used to work with file objects and their positions within a file. These functions are part of the built-in io module, which provides a consistent interface for reading and writing to various file-like objects, such as files, pipes, and in-memory buffers.

# seek() function: The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position.
# Ex:
with open('myfile.txt', 'r') as f:
    print(type(f))
    # Move to the 10th byte in the file
    f.seek(10)

    # Read the next 5 bytes
    data = f.read(8)
    print(data)

f.close()

# Ex 1: Using seek() in Text Mode

f = open("myfile.txt", "r")

f.seek(8)
print(f.tell())
print(f.readline())
f.close()

# Ex 2: Using seek() in Binary Mode with Negative Offset
f = open("myfile.txt", "rb")
f.seek(-10, 2)
print(f.tell())
print(f.readline().decode('utf-8'))
f.close()

# tell() function: The tell() method in Python returns the current position of the file pointer (or cursor) within an open file stream.

with open("myfile.txt", "r") as f:
    print(f.tell())
    data = f.read(4)
    print(data)
    print(f.tell())
f.close()

# Combining tell() with seek(): The tell() method goes hand-in-hand with seek(), which moves the cursor manually.
# Ex:
with open("myfile.txt", "rb") as f:
    f.read(9)   # Advance 9 bytes
    saved_position = f.tell() # Bookmark this spot
    print(saved_position)
    f.read()   # Keep reading further ahead
    f.seek(saved_position) # Telepport right back to the boolmarked spot
f.close()

# truncate() function: When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function.
# Ex:
with open("myfile2,txt", "w") as f:
    f.write('Hello World!')
    f.truncate(12)
with open("myfile.txt", "r") as f:
    print(f.read())

# Ex:
import math

print(math.trunc(3.7))
print(math.trunc(-4.8)) # (flooring would give -4)
print(int(-6.3))  # (built-in int() also truncates floats)