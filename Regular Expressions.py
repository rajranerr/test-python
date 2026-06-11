# Reguler expression: Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.

# 1. Metacharecters: Metacharacters are special characters in regular expressions used to define search patterns. 

# 1. . : Matches any character except a newline.
# 2. ^ : Matches the start of the string.
# 3. $ : Matches the end of the string.
# 4. | : Acts as an OR operator (e.g., a|b). 
# 5. \ : Used to drop the special meaning of character following it.
# 6. []: Represent a character class.
# 7. {}: Indicate the number of occurrences of a preceding regex to match.
# 8. (): Enclose a group of Regex.

# Example:
# 1.Backslash(\): The backslash (\) makes sure that the character is not treated in a special way. This can be considered a way of escaping metacharacters.

# Ex:
import re

s = 'Hello. forpython'

# without using \
match = re.search(r'.', s)
print(match)

# with using \
match = re.search(r'\.', s)
print(match)

# 2. Square Brackets[]: Square Brackets ([]) represent a character class consisting of a set of characters that we wish to match. For example, the character class [abc] will match any single a, b, or c. 

# Ex:
import re

string = "My favorite bikes are interseptor 650 and hunter 350"
pettern = "[a-w]"
result = re.findall(pettern, string)

print(result)

# 3. Caret(^): Caret (^) symbol matches the beginning of the string i.e. checks whether the string starts with the given character(s) or not. 

# Ex:
import re
regex = r'^The'
strings = ['The interseptor 650', 'The hunter 350', 'A ronin 350']

for string in strings:
    if re.match(regex, string):
        print(f'Matched: {string}')
    else:
        print(f'Not matched: {string}')

# 4. Doller($): Dollar($) symbol matches the end of the string i.e checks whether the string ends with the given character(s) or not. 

# Ex:

import re

string = "Hello World!"
pattern = r"World!$"

match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")


# 5. Dot(.): Dot(.) symbol matches only a single character except for the newline character (\n). 

# Ex:

import re

string = "The boy is playing cricket with his friends."
pattern = r"brown.cricket"

match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")

# 2. Charecter Classes and Sequences: Special sequences do not match for the actual character in the string instead it tells the specific location in the search string where the match must occur. It makes it easier to write commonly used patterns.

# 1. \d : Matches any digit [0-9].
# 2. \D : Matches any non-digit.
# 3. \w : Matches any alphanumeric character or underscore [a-zA-Z0-9_].
# 4. \s : Matches any whitespace (spaces, tabs, newlines).
# 5. [A-Z] : Matches any uppercase letter custom range.
# 6. [^0-9] : Matches any character not inside the brackets (negation).
# 7. \A: Matches if the string begins with the given character.

#  3. Quantifiers: 
# 1. * : Zero or more repetitions.
# 2. + : One or more repetitions.
# 3. ? : Zero or one repetition (makes it optional).
# 4. {n} : Exactly n repetitions.
# 5. {m,n} : Between m and n repetitions.


# Examlpe: 
# Extracting Information(re.findall): Extract all phone numbers matching a specific format from a text block: 
# Ex:
import re

text = "Call me at 999-954-6542 or office line 666-965-5654."
# pattern: 3 digits, hyphen, 3 digit, hyphen, 4 digits
pattern = r"\d{3}-\d{3}-\d{4}"

numbers = re.findall(pattern, text)
print(numbers)

# Modifying Strings(re.sub): Anonymize user records by masking digits:

# Ex:
import re

text = "User ID: 83645"
# Replace all digits with an 'X'
clean_text = re.sub(r"\d", "X", text)

print(clean_text)

# Capturing Groups (re.search):Isolate specific structural elements from data fields using parentheses ():

# Ex:
import re

email = "Contact: example@gmail.com"
# Capture username and domain separately
pattern = r"(\w+)@(\w+\.\w+)"

match = re.search(pattern, email)

if match:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))


# Compiling Patterns: If you intend to evaluate the same pattern multiple times across large loops, compile it first using re.compile(). This saves execution time by caching the compiled rules:

# Ex:
import re

# Compile once
compiled_date_pattern = re.compile(r"\d{4}-\d{2}-\d{2}")

# Reuse many times efficiently
is_valid = compiled_date_pattern.match("2010-10-09")

print(is_valid)

# Ex: 
import re
print("Range", re.search(r'[a-zA-Z]', 'x'))

# Code Functions: The re module offers several primary functions for text processing: 

# re.search(pattern, string): Finds the first occurrence of a pattern anywhere. Return: Match object or None.
# re.match(pattern, string): Checks for a match only at the beginning of a string. Return: Match object or None.
# re.findall(pattern, string):	Extracts all non-overlapping matches. Return: List of strings or tuples.
# re.finditer(pattern, string):	Finds all occurrences sequentially. Return:	Iterator yielding Match objects.
# re.sub(pattern, repl, string):	Replaces matches with a new string.	Return: Modified string.
# re.split(pattern, string): Splits a string wherever the pattern matches. Return:	List of substrings.