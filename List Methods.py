# List mathods

#  List.sort(): This mathod sorts the ascending order. The original list is updated
print("1. List.sort Examples: ")
# Ex:
colors = ["black", "white", "blue", "orange", "voilet"]
colors.sort()
print(colors)

# Ex:
num = [4,6,2,5,1,2,1,2,8,9,7]
num.sort()
print(num) 

# reverse(): This method reverses the order of the list.
print("2. reverse Examples: ")
# Ex:
colors.reverse()
print(colors)

# Ex:
num.reverse()
print(num)

# index(): This method returns the idex of the first occurrence of the list item.
print("index Example: ")
# Ex:
print(colors.index("black"))

# Ex:
print(num.index(8))

# count(): Returns the count of the number of the items with the given value.
print("count Examples: ")
# Ex:
print(colors.count("white"))

# Ex:
print(num.count("9"))

# copy(): Return copy of the list. This can be done to perform operation on the list without modifying the original list.
print("Examples of copy: ")
# Ex:
newlist = colors.copy()
print(colors)
print(newlist)
# Ex:
newnum = num.copy()
print(num)
print(newnum)

# append(): This methode items to the end of the existing list.
print("Examples of append: ")
# Ex:
colors.append("indigo")
print(colors)

# Ex:
num.append(12)
print(num)

# insert(): This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method .
print("Example of insert(): ")
# Ex:
colors = ["voilet", "indigo","blue"]
#            [0]      [1]      [2]

colors.insert(1, "black") # insert item at index
# updated list colors is:
print(colors) # output: ["voilet", "black", "indigo", "blue"]
#                  [0]      [1]         [2]      [3]

# extend(): This mathod adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
print("Example of extebd(): ")
# Ex:
colors = ["voilet", "indigo", "black"]
rainbow = ["red", "blue", "yellow", "orange", "green"]
colors.extend(rainbow)
print(colors)

# Concatenating two lists: You can simply concatenate two list to join two list.
# Ex:
colors = ["yellow", "blue", "black", "white"]
colors2 = ["red", "green", "orange", "voilet", "gray", "silver"]
print(colors + colors2)