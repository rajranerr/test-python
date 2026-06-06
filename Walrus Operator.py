# Walrus Operator (:=): The walrus operator (:=), formally known as an assignment expression, allows you to assign a value to a variable inside a larger expression.

# Example 1: Using Walrus Operator in a while Loop
num = [1, 2, 3, 4, 5, 6, 7, 8]

while (n := len(num)) > 0:
    print(num.pop())

# Example 2: Comparing with and without Walrus Operator
d = [
    {"userId": 1, "name": "Raj", "completed": False},
    {"userId": 1, "name": "Suraj", "completed": False},
    {"userId": 1, "name": "Toshnil", "completed": False},
    {"userId": 1, "name": "Kamesh", "completed": True}
]

print("With Python 3.8 Walrus Operator:")
for entry in d:
    if name := entry.get("name"):
        print(name)

print("Without Walrus operator:")
for entry in d:
    name = entry.get("name")
    if name:
        print(name)

# Example 3: Simplifying User Input Loops

# Without Walrus Operator
foods = []
while True:
    f = input("What food do you like?: ")
    if f == "quit":
        break
    foods.append(f)

# With Walrus Operator
foods = []
while (f := input("What food do you like? (type 'quit' to stop): ")) != "quit":
    foods.append(f)