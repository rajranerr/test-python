# String formatting in python
# String formatting can be done in python using the format method.
# Ex:
txt = "for only {price:.2f} dollars!"
print(txt.format(price = 49))

# f-strings:

# It is a new string formatting mechanism introduced by the PEP 498. It is alo know as leteral string interpolation or more commonly as F-strings
#  (f character preceding the string literal). The primary focus of this mechinism is to make the interpolation easier.

#  When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much ssame as the 
#  str.format() method. The f-string offers a convenient way to embed python expression inside string literal for formating.

# Ex:
name = "Raj Rane"
country = "Haidarpur Madhya Pradesh"
print(f"my name is {name} and I am from {country}.")

# Ex:
Hindi = 70
English = 75
mathametics = 85
chemistry = 75
physics = 80
total_subject = Hindi+English+mathametics+chemistry+physics
print(f"Kulalux got total {total_subject} out of 500")
percentage = total_subject/500*100
print(f"{percentage}")