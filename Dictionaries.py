# Dictionaries: Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
# Ex:
info = {'name':'Natash', 'age':19, 'eligible':True}
print(info)

# Ex:
dic = {
    1201:"shivakshi",
    1202:"lakshita",
    1203:"priyanshi",
    1204:"toshnil",
    1205:"om",
    1206:"chetanya",
    1207:"krishna",
    1208:"raj"
}
print(dic[1203])

# Accessing Dictionary items: 
# 1. Accessibg single values: Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in squere brackets or by using get method.

# Ex:
info = {'name':'Aline', 'age':20, 'eligible':True}
print(info['name'])
print(info.get('eligible'))

# 2. Accessing multiple values: We can print all the values in the dictionary using values() method.
# Ex:
info = {'name':'Krishna', 'age':21, 'eligible':False}
print(info.values())
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

# 3. Accessing keys: We can print all the keys in the dictionary using keys() method.
# Ex:
info = {'name':'Roshan', 'age':21, 'eligible':True}
print(info.keys())
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

# 4. Accessing key-value pairs: We can print all the key-value pairs in the dictionary using items() method.
# Ex:
info = {'name':'karan', 'age':19, 'eligible':True}
print(info.items())

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

# Dictionary mathods: Dictionary uses serversl built-in methods for manipulation. They arer listed below

# update(): The update() method updetes the value of the key provided to it if the item already in the dictionary, else it creates a new key-value pair.
# Ex:
info = {'name':'kushu', 'age':18, 'eligible':True}
print(info)
info.update({'age':17})
info.update({'DOB':2010})
print(info)

# Removing items from dictionary: There are a few methods the we can use to remove items from dictionary.

# clear(): The clear() method removes all the items from the list.
# Ex: 
info = {'name':'pratham', 'age':19, 'eligible':True}
info.clear()
print(info)

# pop(): The pop() method removes the key-value pair whose key id passsed as a parameter.
# Ex:
info = {'name':'pranay', 'age':21, 'eligible':True}
info.pop('eligible')
print(info)

# popitem(): The popitem() method removes the last key-value pair from the dictionary.
# Ex:
info = {'name':'parth', 'age':20, 'eligible':True, 'DOB':2006}
info.popitem()
print(info)

# del: We can also use the del keyword to remove a dictionary item.
# Ex:
info = {'name':'yugal', 'age':20, 'eligible':True, 'DOB':2006}
del info['age']
print(info) # If key is not provided, then the del keyword will delete the dictionary entirely.

# Ex:
# info = {'name':'yugal', 'age':20, 'eligible':True, 'DOB':2006}
# del info
# print(info)  # output: NameError: name 'info' is the not defined