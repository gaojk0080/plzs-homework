#!/usr/bin/env python3
import sys
import io

output = io.StringIO()
sys.stdout = output

def my_print(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    print(*args, sep=sep, end=end, file=file, flush=flush)



a = 1
with open('my_print_output.txt', 'w') as f1, open('print_output.txt', 'w') as f2:
    sys.stdout = f1
    my_print('Hello', 'World')
    my_print('1111111', end = " ")
    my_print(f"{a}")
    my_print("222", a)
    sys.stdout = f2
    print('Hello', 'World')
    print('1111111', end = " ")
    print(f"{a}")
    print("222", a)
    
sys.stdout = sys.__stdout__
with open('my_print_output.txt', 'r') as f1, open('print_output.txt', 'r') as f2:
    if f1.read() == f2.read():
        print("The contents of the two files are the same")
    else:
        print("The contents of the two files are inconsistent")
