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

# Ex:
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print("fibonicci: ",fibonacci(20))

# Ex:
def tail_fact(n, acc=1):
    if n == 0:
        return acc
    else:
        return tail_fact(n-1, acc * n)
    
def nontail_fact(n):
    if n == 0:
        return 1
    else:
        return n * nontail_fact(n-1)
print("tail_fact: ",tail_fact(10))
print("nontail_fact: ",nontail_fact(10))