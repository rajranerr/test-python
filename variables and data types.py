# Variables and data types 

# Variables: variable is a container that holds data.Variable is like creating a placeholder in memory  and assigning it some value . In python its as easy as writing.

# a= 1 : it is integer(int)
# b= true or false : it is boolean
# c= "raj" : it is string (str)
# d= none : it is none type variable

# these is four variables of different data type

# Data types : Data types specifies the type of value a variable holds. This is required in programming to do various operation causing an error.
               # In python , we can print the type of any operation using type function.
# type : this function  show which type of variable.
# ex:
a= 1
print(type(a))
b="kula"
print(type(b))
# By defult, python provides the following Bult-in data type

# 1. Numeric data type: int, float , complex

# integer(int): positive, nagetive, and zero numbers. But decimal and fractionals are not.
# int = -2, -1, 0, 1, 2, ...etc.
a =  -2+3
print(a)
# floating point numbers(float): fractional and dicimal numbers.
# float = 0.7236, 0.6, 12/3, 5/2, 0.994, ....etc.
a = 0.724 + 5.34
print(a)
# complex number(complex): A combination of a real numbers and imaginary numbers(a+bi)
# complex: 3+2i,6-7i,24+6i,a+bi, ....etc.
# a = real part : the standard, everyday number (integers and floating point numbers)
# b = imaginary part : the number multiplied by imaginary unit i(often called iota)
# i = imaginary unit : Defined mathematically as the square root of -1. Therefore, i**2 == -1.
# complex : a+bi
a=4
b=5
i = -1
c=a+b*i
print(c)
# 2. Text data type: str

# string(str): 
a = "hello i am raj"
print(a)

# 3. Boolean data type: Represents truth values true or false.
# ex:
is_active = True
print(is_active)


# 4. sequenced data type: list, tuple

# list[]: A list is an ordered collection of data with element separated by comma and enclosed by square breckets[]. List are mutable and can be modified after creation.

# ex:
list1 = [1, 2, 3, [-2,6], ["apple", "mango"]]
print(list1)

# tuple() : A tuple is a immutable. it is cannot be modified or changed after creation.it is enclosed in perentheses().

# ex:
tuple1 = (("parrot", "sparow"),("mango","carry"))
print(tuple1)

# Mapped data type : dict

# dictionary(dict){}: A dictionary is unordered collection of data containing a. key : value pain. it is mutable
 # key value pairs are enclosed in curly brecket{}.

# ex: 
dict1 ={"name": "kulalux", "age": 18, "student" : True }
print(dict1)

# 4 Set types: set

# set{} : Unodered cellection of unique items; automatically removes duplicates. it is mutable.
 # ex:
unique_numbers = {1, 2, 3, 3} 
print(unique_numbers)