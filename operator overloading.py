# Operator overloading: Operator overloading allows you to redefine how built-in mathematical, comparison, and assignment operators behave when used with custom, user-defined objects. This is achieved by defined special method within your class, commonly known as "magic methods" or "dunder methods" (due to their double underscores, like __add__).

# Example:

# Vector Addition and comparison
# Ex:
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Vector):
            self_mag = math.sqrt(self.x**2 + self.y**2)
            other_mag = math.sqrt(other.x**2 + other.y**2)
            return self_mag > other_mag
        return NotImplemented
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = Vector(53, 43)
v2 = Vector(32, 42)

v3 = v1 + v2
print(v3)

print(v1 > v2)

# Common Magic Methods Reference

# 1. Arithmetic Operators

# 2. + → __add__(self, other)
# 3. - → __sub__(self, other)
# 4. * → __mul__(self, other)
# 5. / → __truediv__(self, other)
# 6. // → __floordiv__(self, other)
# 7. % → __mod__(self, other)
# 8. ** → __pow__(self, other)

# Comparison Operators

# 1. < → __lt__(self, other)
# 2. > → __gt__(self, other)
# 3. == → __eq__(self, other)
# 4. != → __ne__(self, other)
# 5. <= → __le__(self, other)
# 6. >= → __ge__(self, other)

# Compound Assignment Operators

# 1. += → __iadd__(self, other)
# 2. -= → __isub__(self, other)
# 3. *= → __imul__(self, other)
# 4. /= → __itruediv__(self, other) 

# Advanced: Handling Reverse (Reflected) Operations

# Ex:
class Price:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Price(self.amount + other)
        return NotImplemented
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __repr__(self):
        return f"${self.amount}"
    
p = Price(8000)
print(p + 100000)
print(120000 + p)

# Ex:
class A:
    def __init__(self, a):
        self.a = a
    
    def __gt__(self, other):
        return self.a > other.a

ob1 = A(65)
ob2 = A(49)
if ob1 > ob2:
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")