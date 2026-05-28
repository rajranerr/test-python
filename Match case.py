# Match case statements: To implement switch-case like characteristics very similar to if-else functionality, 
#          we use a match case in python. if you are coming from a c,c++ or java like laguage, you must have heard of switch-case 
#     statements. If this is your first language, dont worry as i will tell you everything you need to know about match case statement.

#  A match statement will compare a given variable's value to different shapes, also referred to as the
#    pattern. The main idea is to keep on comparing the variable with all the present petterns until it fits
#   into one.

# The match case consists of three main entities:

# 1. the match keyword
# 2. one or more case clauses
# 3. expression for each case

# The case clayse consists of a pattern to be matched to the variable, 
# and a set of statements to be executed if the pattern matches.
 
# Ex:
   
status = 700

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")

# Ex:

def check_number(x):
    match x:
        case 40:
            print("it's 40")
        case 60:
            print("it's 60")
        case _:
            print("it's neither 40 nor 60")

check_number(40)
check_number(80)

# Ex:

def process(data):
    match data:
        case [x, y]:
            # A listb with two elements
            print(f"two-element list: {x}, {y}")
        case [x, y, z]:
            # A list witj three elements
            print(f"Three-element list: {x}, {y}, {z}")
        case _:
            print("Unknown data format")

process([16, 23])
process([15, 4, 32])
process([14, 26, 83, 40])