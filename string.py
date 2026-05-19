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

