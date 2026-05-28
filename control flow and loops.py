# control flow and loops

# conditionals: if, elif and else

# if statement: Executes a block of only if a condition is true.
 # ex:
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote!")

# if-else statement: Provides an alternative blockif the condition is false.
# ex:
age = int(input("Enter a your age: "))
if age >= 18:
    print("adult")
else:
    print("minor")

# if-elif-else statement:
# ex:
score = int(input("Enter score: "))
if score >= 70:
    print("grade A")
elif score >= 60:
    print("grade B")
elif score >= 50:
    print("grade C")
else:
    print("grade D")

# loops : Loop repeat a block of code multiple times.

# for loop: Iterates over a sequence (like a list, string, or range).
# ex:
for i in range(3):
    print(f"iteration {i}")

# while loop : repeats as long as a specified condition remain true.
# ex:
count = 0
while count < 3:
    print(count)
    count += 1


# transfer statements:

# break : Immediately terminates the current loop.
#continue: Skip the rest of the current iteration and moves to the next one.
#pass : A null statement used as a placeholder when syntex required a statement but you don't want to excute any code.

# ex:
for num in range(5):
    if num == 2:
        continue
    if num == 4:
        break
    print(num)