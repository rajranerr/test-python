# Recurtion: Recursion is the process of defining something in terms of itself.

# A physical world example would be to place two parallel mirrors facing ech othor. Any object in between them would be reflected recursively.

# Python Recursive Function 

# we know that function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursin=ve functions.

# Ex:
def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))
    
# driver code
num = 7;
print("number: ",num)
print("Factorial: ",factorial(num))
