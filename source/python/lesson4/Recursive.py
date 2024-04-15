#!/usr/bin/env python3
def get_user_input(function, error):
    while True:
        try:
            user_input = int(input(function))
            if user_input <= 0:
                print(error)
            else:
                return user_input
        except ValueError:
            print(error)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def generate_binomial_coefficients(n):
    coefficients = []
    for i in range(n+1):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(coefficients[i-1][j-1] + coefficients[i-1][j])
            if row[-1] > n:
                return coefficients
        coefficients.append(row)
    return coefficients

def arithmetic_sequence(n, d):
    sequence = []
    for i in range(1, n+1):	
        sequence.append(i*d)
    return sequence

Recursive = [
    {'name':'factorial','func':'factorial', 'params': 1, 'func': factorial,'prompt':'Please enter a positive integer:', 'error':'Enter a valid number!'},
    {'name':'generate_binomial_coefficients','params' : 1, 'func': generate_binomial_coefficients,'prompt':'Enter the maximum value', 'error':'Enter a valid'},
    {'name':'arithmetic_progression', 'params': 2,'func': arithmetic_sequence,'prompt':'Enter the maximum value and tolerance in turn:', 'error':'Enter a valid number'}
]
while True:
    for i, formula in enumerate(Recursive):
        print(f"{i+1}. {formula['name']}")
    choice = get_user_input("Choose a formula:", "Error!Choose an existing formula！") - 1
    
    if(choice == -1):
        break
    formula = Recursive[choice]
    params = []
    for i in range(formula['params']):
         qwq = get_user_input(formula['prompt'], formula['error'])
         params.append(qwq)
    result = formula['func'](*params)
    print(f"计算结果：{result}")
