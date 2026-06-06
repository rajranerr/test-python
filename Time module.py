# Time module: Time Module is a built-in library used for handling time-related tasks, tracking execution duration, and adding execution delays. It works on the concept of Unix time (seconds elapsed since the epoch of January 1, 1970).

# Example:

# 1. Adding a Delay: Use time.sleep() to halt code execution. It accepts fractional inputs for sub-second precision.
# Ex:
import time

print("Task started...")
time.sleep(20.6)
print("Task finished")

# 2. Measuring Code Execution Time: For benchmarking performance, use time.perf_counter() instead of time.time(), as it provides the highest available resolution and ignores system clock changes.
# Ex:
import time

start_time = time.perf_counter()

for _ in range(2_000_000):
    pass

end_time = time.perf_counter()
print(f"Execution time: {end_time - start_time:.5f}seconds")

# 3. Formatting Time structures into Clean strings: Convert a raw timestamp into a readable format using time.localtime() and time.strftime().
# Ex:
import time

current_struct = time.localtime()

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_struct)
print("Readable Date:", formatted_time)

# Ex:
import time
print(time.gmtime(10))

# Ex:
import time
for i in range(6):
    time.sleep(2)
    print(i)

# Ex:
import time
current = time.time()
print("Current time in seconds since epoch =", current)

# Ex:
import time
current = time.ctime(1780740495.8793995)
print("Current time:", current)

# Ex:
import time
obj = time.localtime(1780740495.8793995)
print(obj)

# Ex:
import time
obj1 = time.gmtime(1780740495.8793995)
time_sec = time.mktime(obj1)
print("Local time (in seconds):", time_sec)