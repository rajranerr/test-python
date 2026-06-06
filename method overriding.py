# Method overriding: Method overriding occurs when a child class defines a method with the same name and signature as a method in its parent class. It allows the child class to provide a specific implementation of that method, changing or extending the parent class's behavior. This concept is a core element of object-oriented programming (OOP) and enables runtime polymorphism. 

# Example:
class Parent:
    def show_message(self):
        print("This is the parent method.")

class Child(Parent):
    # Overrinding the parent method
    def show_message(self):
        print("This is the overridden method in the child class.")

# Instance of child calls the overridden method 
obj = Child()
obj.show_message()

# Ex:
class Employee:
    def work(self):
        print("Processing basic administrative tasks.")

class Manager(Employee):
    def work(self):
        # Call the parent method first
        super().work()
        # Add manager-specific tasks
        print("Approving budget requests and scheduling team syncs.")

mgr = Manager()
mgr.work()

# Overriding Constructors (__init__): A common real-world use case is overriding the __init__ constructor method. If you redefine __init__ in a subclass, you must call super().__init__() to ensure attributes from the parent class are correctly initialized: 

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class ElectricCar(Vehicle):
    def __init__(self, brand, battery_capacity):
        # Initialize parent attributes
        super().__init__(brand)
        # Initialize child attributes
        self.battery_capacity = battery_capacity

# battery_capacity = 100
# brand = "OnePlus"
# print(battery_capacity)
# print(brand)

# Preventing method Overriding
# Ex:
from typing import final

class DatabaseConnection:
    @final
    def connect(self):
        print("Establishing secure connection...")

# Using Super()

# Ex:
class Parent(): 
	
	def show(self): 
		print("Inside Parent") 
		
class Child(Parent): 
	
	def show(self): 
          
          super().show()
          print("Inside Child")

obj = Child()
obj.show()

# Ex:
# function in multiple inheritance 
class GFG1: 
	def __init__(self): 
		print('HEY !!!!!! GfG I am initialised(Class GEG1)') 
	
	def sub_GFG(self, b): 
		print('Printing from class GFG1:', b) 
	
# class GFG2 inherits the GFG1 
class GFG2(GFG1): 
	def __init__(self): 
		print('HEY !!!!!! GfG I am initialised(Class GEG2)') 
		super().__init__() 
	
	def sub_GFG(self, b): 
		print('Printing from class GFG2:', b) 
		super().sub_GFG(b + 1) 
	
# class GFG3 inherits the GFG1 ang GFG2 both 
class GFG3(GFG2): 
	def __init__(self): 
		print('HEY !!!!!! GfG I am initialised(Class GEG3)') 
		super().__init__() 
	
	def sub_GFG(self, b): 
		print('Printing from class GFG3:', b) 
		super().sub_GFG(b + 1) 
	
	
# main function 
if __name__ == '__main__': 
	
	# created the object gfg 
	gfg = GFG3() 
	
	# calling the function sub_GFG3() from class GHG3 
	# which inherits both GFG1 and GFG2 classes 
	gfg.sub_GFG(16)