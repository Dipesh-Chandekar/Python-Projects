"""
Decorators
Create a decorator time_decorator that measures the
time a function takes to execute. Apply
this decorator to a function calculate_sum(n) that
calculates the sum of numbers from 1 to n.
Example:
@time_decorator
def calculate_sum(n):
return sum(range(1, n+1))
print(calculate_sum(1000000))
# Output: (Execution time and the sum result)
"""

import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() # captures the current time before func is called.
        result = func(*args, **kwargs) # executes the function with any arguments and keyword arguments.
        end_time = time.time() # captures the current time after func finishes executing.
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
        return result
    return wrapper

@time_decorator # to measure and print the execution time of the decorated function.
def calculate_sum(n):
    return sum(range(1, n + 1))

print("This function will return the time taken to execution the function.")
print(calculate_sum(1000000))
