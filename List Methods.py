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