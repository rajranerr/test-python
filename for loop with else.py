# else in loop:
# As you have learned before, the else clause is used along with the if statement.

# Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.

# Syntax: 
# for counter in sequence:
    # Statements in side for loop block
# else:
    # Statement inside else block

# Ex:
for x in range(6):
    print("iteration no {} in for loop". format(x+1))
else:
    print("else block in loop")
print("Out of loop")

# Examples:

# 1. Searching a list: A common use case is searching for an item. The else block handle the the "not found" logic without needing a separate flag variable.

numbers = [1, 2, 4, 6, 8]
target = 3

for num in numbers:
    if num == target:
        print(f"found {target}!")
        break
else:
    # this runs because 4 is not in the list, so 'break' never happens
    print(f"could no find {target} in the list.")