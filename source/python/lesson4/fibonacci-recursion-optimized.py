#!/usr/bin/env python3
fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    
    if n <= 1:
        return n
    
    fib_value = fibonacci(n-1) + fibonacci(n-2)
    fib_cache[n] = fib_value
    
    return fib_value

while True:
        try:
            num = int(input("Please input a positive integer："))
            if num <= 0:
                print("Error, Please input a positive integer!")
            else:
                break
        except ValueError:
            print("Error, Please input a positive integer！")

fibonacci_sequence = []
for i in range(num+1):
    fib_num = fibonacci(i)
    if fib_num > num:
        break
    fibonacci_sequence.append(fib_num)

print(f"The Fibonacci numbers less than {num}:{fibonacci_sequence}")
