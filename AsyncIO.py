# AsyncOI: asyncio is a built-in Python library used to write concurrent code using the async and await syntax.

# Core Components

# Coroutines: Functions defined with async def. Calling them creates a coroutine object instead of executing the code immediately.
# The Event Loop: The central manager or "orchestra conductor" of an async program. It schedules tasks, listens for external events, and switches between coroutines when they pause.
# Awaitables: Objects you can use with the await keyword (mainly coroutines, Tasks, and Futures). await pauses execution until the awaited object completes. 
# Tasks: Wrappers that schedule a coroutine to run concurrently on the event loop as soon as possible. 

# Example: 
# import asyncio

# async def fetch_data(task_id: int, delay: int):
#     print(f"Task {task_id}: Starting...")
#     # Yields control to the event loop, simulating a network request
#     await asyncio.sleep(delay) 
#     print(f"Task {task_id}: Data fetched!")
#     return f"Result {task_id}"

# async def main():
#     # Modern approach (Python 3.11+) to handle structured concurrency safely
#     async with asyncio.TaskGroup() as tg:
#         task1 = tg.create_task(fetch_data(1, 2))
#         task2 = tg.create_task(fetch_data(2, 3))
#         task3 = tg.create_task(fetch_data(3, 4))
#         task4 = tg.create_task(fetch_data(4, 1))
        
#     # Execution pauses here until all tasks in the TaskGroup finish
#     print("All tasks finished.")
#     print(f"Collected: {task1.result()}, {task2.result()}, {task3.result()}, {task4.result()}")

# Entry point to execute the main coroutine
# asyncio.run(main())

# Ex:
import asyncio

async def fn():
    
    print("one")
    await asyncio.sleep(1)
    await fn2()
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)

async def fn2():
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")
asyncio.run(fn())

# Ex:

import asyncio
async def fn():
    task=asyncio.create_task(fn2())
    print("one")
    #await asyncio.sleep(1)
    #await fn2()
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)

async def fn2():
    #await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")
    
asyncio.run(fn())