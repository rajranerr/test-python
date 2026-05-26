# sets: A set is an unordered collection of unique items. Sets are defined using curly braces {} or the set() constructor.

# Unordered: Items do not have a foixed position and cannot be accessed by index.
# unique: Duplicate values are automatically removed.
# mutable: You can add or remove items, but the themselves must be immutable (like strings or numbers).

# Ex:
# 1. creating a Set
# Direct creation with curly braces
fruits = {"apple", "banana", "cherry"}
print(fruits)
# Removing deplicates automatically
numbers = {1,2,2,3,4,4,5,6,6}
print(numbers)

#  creating an empty set (must use set(), not{})
empty_set = set()
print(empty_set)
# Ex:
# Adding and Removing items
colors = {"red", "yellow", "white", "black", "silver"}
print(colors)

# Adding a single item
colors.add("voilet")
print('set after updating:',colors)

# Removing an item (raises error if not found)
colors.remove("yellow")
print('\nset after updating:',colors)

# Removing safely (no error if not found)
colors.discard("blue")
print('\nset after updating:',colors)

# Popping element from the set
print('\nPopped element',colors.pop())
print('Set after updating:',colors)

# clear set itams
colors.clear()
print('\nSet after updating:',colors)

# Ex:
# Using a for loop
info = {"carla", 19, False, 5.9}
for item in info:
    print(item)

# Ex:
alice = set()
print(type(alice))

# Joining Sets: Set in python more or less work in the same way as sets in mathematics. We can perform operation like uion and intersection on the just like in mathematics.
#  1. union() and update(): The union() methods print all items that are present in the two sets. The union() method return a new set whereas update() method adds item into the existing set from another set.
# Ex:
cities = {"Tokyo", "Berlin", "Delhi", "Pune", "Indore"}
cities2 = {"Bhopal", "Tokyo", "Mumbai", "Ratlam", "kolhapur"}
cities3 = cities.union(cities2)
print(cities3)

# Ex:
s1 = {1, 2, 5, 7}
s2 = {3, 4, 6, 8}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)

# 2. intersection and intersection_update(): The intersection0 and intersection_update0 methods prints only items that are similar to both the sets.
#  The intersection0 method returns a new set whereas intersection_update0 method updates into the existing set from another set. 
# Ex:
colors = {"black", "voilet", "silver", "white", "red"}
colors2 = {"yellow", "white", "blue", "black", "gray", "silver", "red"}
colors3 = colors.intersection(colors2)
print(colors3)

colors.intersection_update(colors2)
print(colors)

# 3. symmetric_difference and symmetric_difference_update(): The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
# Ex: 
numbers = {1, 4, 5, 8, 10}
numbers2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12}
numbers3 = numbers.symmetric_difference(numbers2)
print(numbers3)
numbers.symmetric_difference_update(numbers2)
print(numbers)

# 4. difference() and difference_update(): The difference0 and difference_update0) methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
# Ex: 
name = {"toshnil", "suraj", "bhupesh", "raj", "darshan", "kamesh", "kartik"}
name2 = {"kartik", "gaurav", "lomesh", "soham", "suraj"}
name3 = name.difference(name2)
print(name3)
name.difference_update(name2)
print(name)

# Set Methode: There are several in-built methods used for the manipulation of set.They are explained below

# isdisjoint(): The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
# Ex: 
fruits = {"apple", "banana", "graps", "cherry"}
fruits2 = {"orange", "banana", "apple", "graps"}
print(fruits.isdisjoint(fruits2))

# issuperset(): The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
# Ex:
team = {"sagar", "harshal", "kamesh", "soham", "toshal"}
team2 = {"yojan", "bhopesh", "nupur", "bhomesh", "bhushan"}
print(team.issuperset(team2))
team3 = {"gaurav", "toshnil", "raj", "suraj", "parth", "uday"}
print(team.issuperset(team3))

# issubset(): The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
# Ex:
cities = {"bhopal", "indore", "nagpur", "ratlam"}
cities2 = {"indore", "bhopal"}
print(cities2.issubset(cities))

# add(): If you want to add a simgle item to the set use the add() method.
#  Ex:
cities = {"bhopal", "indore", "nagpur", "ratlam", "pune"}
cities.add("akola")
print(cities)

# update(): If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update0 method to add it into the existing set.
cities = {"bhopal", "indore", "nagpur", "ratlam", "pune"}
cities2 ={"mumbai", "dehli", "gurugram"}
cities.update(cities2)
print(cities)