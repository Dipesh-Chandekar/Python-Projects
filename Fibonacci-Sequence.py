"""
Generators
Write a generator function fibonacci_sequence(n) that
generates the Fibonacci sequence up to
the n-th number. The function should yield one
Fibonacci number at a time.

Example:
for num in fibonacci_sequence(10):
print(num)
# Output: 0 1 1 2 3 5 8 13 21 34
"""

def fibonacci_sequence(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

if __name__ == '__main__':
    n = int(input("Enter the number of Fibonacci sequence elements to generate: "))
    for num in fibonacci_sequence(n):
        print(num)
