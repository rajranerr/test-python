# MultiProcessing: The multiprocessing module in Python allows you to run multiple tasks completely in parallel by allocating them to separate operating system processes.

# 1. The process Class: Use the Process class to manually create and manage individual workers. This approach gives you complete control over process lifecycles.
# Ex:
import multiprocessing
import os
import time

def compute_square(number):
    print(f"Child Process ID: {os.getpid()} calculating...")
    time.sleep(1)
    print(f"Square: {number * number}")

if __name__ == "__main__":
    # 1. Create the process object
    process = multiprocessing.Process(target=compute_square, args=(20,))
    
    # 2. Start the process execution
    process.start()
    
    # 3. Wait for the process to complete before moving forward
    process.join()
    print("Main process finished.")

# 2. The pool Class: Use a Pool when you want to distribute a dataset or parallelize a loop across a fixed batch of worker processes. The pool manages worker lifetimes automatically.

# Ex:
import multiprocessing

def compute_cube(number):
    return number ** 3

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # Automatically scales to the number of CPU cores available
    with multiprocessing.Pool() as pool:
        # pool.map splits the list and runs tasks in parallel
        results = pool.map(compute_cube, numbers)
        
    print(f"Results: {results}")

# 3. Inter-Process Communication (IPC): Because processes do not share memory, they cannot modify the same global variables. The standard library provides specific tools to securely pass data across process boundaries:

# Queue: A thread- and process-safe FIFO data structure that pickles objects to transmit them.
# Pipe: A fast, direct two-way connection channel between exactly two processes.
# Manager: A server-controlled process allowing you to share high-level Python objects like lists and dictionaries. 

# Ex:

import multiprocessing

def worker(queue):
    queue.put("Data sent from child process!")

if __name__ == "__main__":
    communication_queue = multiprocessing.Queue()
    
    p = multiprocessing.Process(target=worker, args=(communication_queue,))
    p.start()
    
    # Retrieve data in the main process
    message = communication_queue.get()
    p.join()
    
    print(message)

# Ex:

# importing the multiprocessing module
import multiprocessing

def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))

def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))

if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=(30, ))
    p2 = multiprocessing.Process(target=print_cube, args=(30, ))

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    # both processes finished
    print("Done!")

# Ex:

# importing the multiprocessing module
import multiprocessing
import os

def worker1():
    # printing process id
    print("ID of process running worker1: {}".format(os.getpid()))

def worker2():
    # printing process id
    print("ID of process running worker2: {}".format(os.getpid()))

if __name__ == "__main__":
    # printing main program process id
    print("ID of main process: {}".format(os.getpid()))

    # creating processes
    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)

    # starting processes
    p1.start()
    p2.start()

    # process IDs
    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))

    # wait until processes are finished
    p1.join()
    p2.join()

    # both processes finished
    print("Both processes finished execution!")

    # check if processes are alive
    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))