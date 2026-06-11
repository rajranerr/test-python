# Multithreading: Multithreading in Python allows a program to run multiple threads (smaller units of a process) concurrently within a single process to handle multiple tasks at the same time. 

# Example:

import threading
import time

def fetch_data(source_name, delay):
    """A sample worker function that simulates fetching data from the web."""
    print(f"[+] Fetching data from {source_name}...")
    time.sleep(delay)  # Simulates network/IO block
    print(f"[✓] Finished fetching from {source_name}!")

# Define the targets and arguments
targets = [("API_1", 2), ("API_2", 3), ("API_3", 1)]
threads = []

start_time = time.time()

# 1. Create and start the threads
for name, delay in targets:
    # target: function to run, args: arguments passed as a tuple
    thread = threading.Thread(target=fetch_data, args=(name, delay))
    threads.append(thread)
    thread.start()  # Initiates the thread execution

# 2. Wait for all threads to finish before moving forward
for thread in threads:
    thread.join()  # Main program halts here until this specific thread completes

end_time = time.time()
print(f"\nAll tasks finished in {end_time - start_time:.2f} seconds!")

# A Modern Alternative: ThereadpoolExacutor

# Ex:
# from concurrent.futures import ThreadPoolExecutor
# import time

# def process_item(item):
#     print(f"Processing {item}")
#     time.sleep(1)
#     return f"Result for {item}"

# items = ['A', 'B', 'C', 'D', 'E']

# # Creates a pool of up to 3 worker threads
# with ThreadPoolExecutor(max_workers=3) as executor:
#     # executor.map automatically assigns items to threads and collects results
#     results = executor.map(process_item, items)

# print(list(results))

# Ex:
# import threading
# import time

# def square(num):
#     print(f"Square: {num*num}")
#     time.sleep(1)

# def cube(num):
#     print(f"Cube: {num*num*num}")
#     time.sleep(1)

# t1 = threading.Thread(target=square, args=(6,))
# t2 = threading.Thread(target=cube, args=(6,))

# t1.start()
# t2.start()
# t1.join()
# t2.join()

# print("Done!")

# # Ex:

# from concurrent.futures import ThreadPoolExecutor

# def worker(task):
#     print(f"Task {task} running")


# # Create a thread pool with 2 workers
# with ThreadPoolExecutor(max_workers=2) as executor:
#     # Submit two tasks to run in parallel
    # executor.submit(worker, 1)
    # executor.submit(worker, 2)
    # executor.submit(worker, 3)