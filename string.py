# string: a string is a sequence of characters used to store and represent text.
#        It is one of the most fundamental
#       data types in the language and is represented by the str class.

# Immutable: Once created, a string's content cannot be changed. Any modification (like appending or replacing) results in the creation of a completely new string.
# Sequence Type: Strings are ordered, meaning each character has a specific position (index).
# Unicode Support: Python strings are sequences of Unicode characters, allowing them to represent text from almost any language.

# creating strings:

# you can creat string by enclosed text in quots:

# single quotes: 'hello'
# double quotes: "hello"
# triple quotes: """multi-line text""" or '''multi-line text'''(useful for text spanning several lines).

# Common Operations:

# python provides many built-in string methods and opraturs for manipulation :
 
# indexing: : Access individual characters using brackets, starting at 0 for the first character (e.g., text[0]).
# Slicing: Extract a portion of a string using text[start:end].Concatenation: Combine strings using the + operator.
# Formatting: Use f-strings (e.g., f"Hello, {name}") to insert variables directly into strings.
# Built-in Methods: Operations like .upper(), .lower(), .strip() (removing whitespace), and .replace(). 

# string is difine as a duble quotes.

# Ex:

text = "Hello,Kulalux"
print(text[6])
print(text.upper())
print(len(text))

# string slicing:

name = "Hello,Kula"
print(len(name))
print(name[6:10])
 
# String as an array:
# A string is essentialty a sequence of characters also called an array. thus we can access the element of this array.
 
# Ex:

ple = "Appleple"
print(ple[:4])
print(ple[7]) # returns at specified index

# string methods:
 # Python provide a set of built-in methods that we can to after and modify the strings.

 # Upper(): THe upper() method converts a string to upper case.

 # Ex:
  
str1 = "hello,kulalux"
print(str1.upper())

# Lower(): The lower() method converts astring to lower case.
# Ex:

str2 ="Hello,Raj"
print(str2.lower())

# length(len): the len() method find string's length.
print(len(str2))

# rstrip(): the rstrip removes any trailing characters.
# Ex:

str3 = "kulalux !!!"
print(str3.rstrip("!"))

# replace(): The replace() methode replace all occurences of a string with another string.
# Ex:
str4 = "silver bike"
print(str4.replace("silver", "black"))

# split(): the split() method split the given string at the specified instance and return the separated the string as list items.
# Ex:

str5 = "my favorite bike is intersepter 650"
print(str5.split(" "))

# capitalize():  method converts the first character of a string to uppercase and all remaining characters to lowercase.
# Ex:
print(str5.capitalize())

# Center(): the center() method sligns the string to the center as per the parameters given by the user.
# Ex:
print(str5.center(50))

# count(): the methode returns the number of lines the given value has occured within the given string.
# Ex:
print(str5.count("i"))

# endswith(): The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
# Ex:
print(str5.endswith("!!!"))
print(str5.endswith("650"))

# find(): The find() mathod searches for the first occurrence of the given value
#         and return the index where it is present. if given value is absent from the string the return -1.
# Ex:
print(str5.find("bike"))

# index(): the index() method searches for the first occurrence of the given value 
#        and return the index where it is present. If given value is absent from the string then raise an exception.
# Ex:
print(str5.index("is"))

# isalnum(): the isalnum() method is a built-in string function used to check if a string consists entirely of alphanumeric characters.
#         It returns a Boolean value (True or False) based on the content of the string.
# Alphanumeric Definition: A character is considered alphanumeric if it is either a letter (A-Z, a-z) or a number (0-9).
# Return Values:True: If all characters in the string are alphanumeric and there is at least one character.
# False: If the string is empty or contains at least one non-alphanumeric character, such as spaces, punctuation, or special symbols (e.g., !, @, #).
# No Parameters: The method does not take any arguments.
# Ex:
print(str5.isalnum())

# isalpha(): The isalnum() methode returns True only if the entire string only consists
#     of A-Z, a-z. if any other characters or puntuations or numbers(0-9) are present, then itv return False.
# Ex:
print(str5.isalpha())

# islower():



