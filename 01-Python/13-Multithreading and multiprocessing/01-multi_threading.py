### Multithreading
## When to use Multi Threading
###I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

##create 2 threads
t1=threading.Thread(target=print_numbers)  ## create a thread and call it t1 whose job is to execute print_numbers.
t2=threading.Thread(target=print_letter) ## create a thread and call it t2

t=time.time() ##gives us the current time
## start the thread
t1.start()
t2.start()

### Wait for the threads to complete
t1.join() ## main program wait for t1 to finish
t2.join() ## main program wait for t2 to finish

finished_time=time.time()-t
print(finished_time)
