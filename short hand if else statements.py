# If ... Else in One line: There is also a shrorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short. Here's an examlpe:
a = 2
b = 330
print("A") if a > b else print("B")

# You can aslo have mulptiple else statements else on the same line:

#  Ex:

# One can also have multiple else statements on the same line:
# Common Examples:

# 1. Short Hand if (No else): if you only have one statement to execute when a condition is true, you can put it on the same line as the if statement:
a = 22
b = 18
if a > b: print("a is greater") 

# Ex: 
age = 20
if age >= 18: print("Eligible to vote.")

# if statement:  If statement is used to execute a block of code only when a specified condition evaluates to True.
age = 18
if age > 18: 
    print("Eligible to vote.")


# 2. Ternary Conditional Statement: This is the most common use case, making code more concise for simple value assignments.
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

# Ex:
a = 10
b = 5
bigger = a if a > b else b
print("bigger")

# if-else statement: If Else statement is used to execute one block of code when the condition is True and another block when the condition is False.
age = 18
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

# 3. Multiple Outcomes (Nested Ternary): You can chain multiple condions to simulate an if-else-elif ladder, though this can become hard to read if overused.
a = 330
b = 330
print("A") if a < b else print("=") if a == b else print("B")

# Ex:
age = 70
is_member = True
if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

# if-elif-else statement: elif statement is used to check multiple conditions in a program. It executes a block of code when its condition evaluates to True after previous conditions evaluate to False.
age = 21
if age <= 12:
    print("Child.")
elif age <= 19:
    print("teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

# Match-case Statement: Match-case statement is used to compare a value against multiple patterns and execute the matching block of code. It is similar to the switch-case statement available in other programming languages.
number = 2
match number:
    case 1:
        print("One")
    case 2|3:
        print("Two or Three")
    case _:
        print("Other number")

# Another Example:
# result = value_if_true if condition else value_if_false

# This syntax is equivealent to the following if-else statement:
a = 24
b = 62
if a >= b:
    print("Value_if_true")
    
else:
    print("Value_if_Falue")

# Conclusion: The shorthand syntax can be a convenient way to write simple if-else statements, especially when you want to assign a value to a variable based on a condition. However, it's not suitable for more complex situations where you need to execute multiple statements or perform more complex logic. In those cases, it's best to use the full if-else syntax.