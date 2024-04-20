#!/usr/bin/env python3
import sys
import io

output = io.StringIO()
sys.stdout = output

def my_print(*args, sep=' ', end='\n'):
    file = open("my_print_output.txt", "a")
    content = sep.join(map(str, args)) + end
    file.write(content)
    file.close()

file = open("my_print_output.txt", "w")
file.close()
a = 1
my_print('Hello, World')
my_print('1111111', end = " ")
my_print(f"{a}") 
my_print("222", a)

with open('print_output.txt', 'w') as f1:
    sys.stdout = f1
    print('Hello, World')
    print('1111111', end = " ")
    print(f"{a}")
    print("222", a)
    
sys.stdout = sys.__stdout__
with open('my_print_output.txt', 'r') as f1, open('print_output.txt', 'r') as f2:
    if f1.read() == f2.read():
        print("The contents of the two files are the same")
    else:
        print("The contents of the two files are inconsistent")
