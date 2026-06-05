# Access Specifiers/Modifiers: Access specifiers or access modifiers in python programming are used to imit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

# Let us see the each one of access specifiers in detail:

# Types of access specifiers:

# 1. Public access modifier: By default, every attribute and method in a Python class is public. They can be freely read, modified, and called from outside the class instance. 

# Ex:
class Account:
    def __init__(self, username):
        self.username = username # Public attribute

acc = Account("Kavya")
print(acc.username)

# Ex:
class Geek:
    def __init__(self, name, age):
        self.geekName = name      
        self.geekAge = age        
    def displayAge(self):        
        print("Age:", self.geekAge)

obj = Geek("Kavya", 18)

print("Name:", obj.geekName)
obj.displayAge()

# 2. Protected Access Modifier: A member is considered protected if its name begins with a single leading underscore (_).
# Ex:
class Account:
    def __init__(self):
        self._database_id = 6987  # Protected attribute

acc = Account()
print(acc._database_id)

# Ex:
class Student:
    def __init__(self, name, roll, branch):
        self._name = name            
        self._roll = roll           
        self._branch = branch       

    def _displayRollAndBranch(self): 
        print("Roll:", self._roll)
        print("Branch:", self._branch)


class Geek(Student):
    def displayDetails(self):
        print("Name:", self._name)  
        self._displayRollAndBranch() 


obj = Geek("Kavya", 10070916, "AI/ML")
obj.displayDetails()

# Private Access Modifier: A member is intended to be private if its name begins with a double leading underscore (__) without a trailing double underscore.
# Ex:
class Account:
    def __init__(self, pin):
        self.__pin = pin  # Private attribute

acc = Account(1605)
# print(acc.__pin)  # Raises AttributeError!

# Bypassing using Name Mangling
print(acc._Account__pin)

# Ex:
class Geek:
    def __init__(self, name, roll, branch):
        self.__name = name         
        self.__roll = roll          
        self.__branch = branch     

    def __displayDetails(self):     
        print("Name:", self.__name)
        print("Roll:", self.__roll)
        print("Branch:", self.__branch)

    def accessPrivateFunction(self):
        self.__displayDetails()    


obj = Geek("Rajesh", 10090716, "AI/ML")
obj.accessPrivateFunction()
print(obj._Geek__name)

# Using all Access Modifiers
# Ex:

class Super:
    publicData = "Public Data Member"
    _protectedData = "Protected Data Member"
    __privateData = "Private Data Member"

    def accessPrivateMembers(self):
        print("Accessing inside class:", self.__privateData)


class Sub(Super):
    def accessProtectedMembers(self):
        print("Accessing inside subclass:", self._protectedData)

obj = Sub()

print(obj.publicData)
print(obj._protectedData)
obj.accessPrivateMembers()
print(obj._Super__privateData)