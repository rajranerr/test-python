# Enumarate function: The enumarate() function in python is a built-in tool that adds a counter to an iterable (like a list, or string) and returns it as an enumerate object. This object can then be used directly in loop to track both the index and the value of items simultaneously without manually managing a counter variable.

# Syntax:
#  The basic syntax for the function is: enumerate(iterable, start=0)

# itarable: Any sequence or collection that supports iteration (e.g., Python List, string, or tuple).
# start (optional): The number from which the counter starts. The defualt is 0.

# Example: This code shows how enumerate() provides both index and value while iterating over a list.

print("Example number 1")
fruits = ['apple', 'banana', 'cherry', 'mango']

# standard usege starting from 0
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Ex:
print("Example number 2.")
names = ["Nimish", "Krishna", "Om", "Rituraj", "Ayush"]
for i, v in enumerate(names): 
    print(i, v)

# Explanation: enumerate(name) return pairs of (index, value), which are unpacked into i and v.

# Syntex: enumerate(iterable, start=0)

# Parameters:
# iterable: sequencce or collection to iterate over.
# start(optional): starting value of the index. Default is 0.

# Return: Return an enumerate object thet generates (index, element) pairs.

# Examples:
# Ex 1: This code converts the enumerate object into a list of tuple. Each tuple contain the index and corresponding element from the list.

alphabets = ["A", "B", "C", "D", "E"]
r = list(enumerate(alphabets))
print(r)

# Explanation: list(enumerate(alphabets)) converts index-element pairs into a list of tuples.

# Ex 2: This code retrieves elements one by using. next(). on enumerate object.

names =["Darshan", "Kamesh", "Soham", "Akhilesh", "Parth", "Lala"]
e = enumerate(names)

print(next(e))
print(next(e))
print(next(e))

# Explanation: next(names) return the next(index, element) pair.

# Ex 3: This code enumerates dictionary. items and provides index with key-value pairs.

marks = {"Suraj": 85, "Toshnil": 90, "Lomesh": 50, "Raj": 60}
for i, (k, v) in enumerate(marks.items()):
    print(i, k, v)

# Explanation: enumerate(d.items()) returns index with (key, value) pairs.