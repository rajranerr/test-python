# Function caching: Function caching is an optimization technique used to store the result of expensive function calls and return the cached result when the same inputs occur again. You can implement it instantly using decorators from the built-in functools module.

# The built-in Options: Python offers two primary built-in decorators for memory-based function caching.

# @functools.cache:   An unbounded cache that grows indefinitely. It is best used when you have a finite number of inputs or plenty of RAM.

# @functools.Iru_cache: : A bounded cache that drops the Least Recently Used items when it hits its size limit. It is ideal for long-running processes to prevent memory leaks.

# Example:
# import time
# from functools import Iru_cache

# @Iru_cache(maxsize=128)
# def network_request(user_id):
#     time.sleep(6)
#     return f"Data for user {user_id}"

# # First execution takes 2 seconds (Cache Miss)
# print(network_request(46))

# # Second execution is instant (Cache Hit)
# print(network_request(46))

# Ex:
from functools import lru_cache
import time

# Function that computes Fibonacci 
# numbers without lru_cache
def fib_without_cache(n):
    if n < 2:
        return n
    return fib_without_cache(n-1) + fib_without_cache(n-2)
    
# Execution start time
begin = time.time()
fib_without_cache(30)

# Execution end time
end = time.time()

print("Time taken to execute the\
function without lru_cache is", end-begin)

# Function that computes Fibonacci
# numbers with lru_cache
@lru_cache(maxsize = 128)
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n-1) + fib_with_cache(n-2)
    
begin = time.time()
fib_with_cache(30)
end = time.time()

print("Time taken to execute the \
function with lru_cache is", end-begin)

# Ex:
from functools import lru_cache

@lru_cache(maxsize = 200)
def count_vowels(sentence):
    sentence = sentence.casefold()
    return sum(sentence.count(vowel) for vowel in 'aeiou')
    
print(count_vowels("Welcome to python practice"))

# Ex: 
from functools import Iru_cache 
import time

@Iru_cache(maxsize=None)
def fx(n):
    time.sleep(6)
    return n*6

print(fx(20))
print("done for 20")
print(fx(32))
print("done for 32")
print(fx(3))
print("done for 3")