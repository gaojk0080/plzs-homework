#!/usr/bin/env python3
import math

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

class Square:
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        return 4 * self.side
    
    def calculate_area(self):
        return self.side ** 2

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
    def calculate_area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

class Ellipse:
    def __init__(self, major_axis, minor_axis):
        self.major_axis = major_axis
        self.minor_axis = minor_axis
    
    def calculate_perimeter(self):
        a = self.major_axis / 2
        b = self.minor_axis / 2
        h = ((a - b) ** 2) / ((a + b) ** 2)
        perimeter = math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
        return perimeter
    
    def calculate_area(self):
        return math.pi * self.major_axis * self.minor_axis

formulas = [
    {'name': 'perimeter and area of square', 'class':Square, 'params': 1, 'prompt': 'Please enter the side length of the square：'},
    {'name': 'perimeter and area of triangle', 'class':Triangle, 'params': 3, 'prompt': 'Please enter the three sides of the triangle in turn：'},
    {'name': 'perimeter and area of rectangle', 'class':Rectangle,  'params': 2, 'prompt': 'Please enter the length and width of the rectangle：'},
    {'name': 'perimeter and area of circle', 'class':Circle,  'params': 1, 'prompt': 'Please enter the radius of the circle：'},
    {'name': 'perimeter and area of ellipse', 'class':Ellipse,  'params': 2, 'prompt': 'Please enter the length of the long axis and the length of the short axis of the ellipse：'}
]

qeq = 0
while(1):
    print("Optional geometric formulas：")
    print(f"0. exit")
    for i, formula in enumerate(formulas):
        print(f"{i+1}. {formula['name']}")
    while True:
        try:
            choice = int(input("Please select a formula：")) - 1
            if(choice == -1):
                break
            if choice >4 or choice <-1:
                print("error，Please enter an existing formula！")
            else:
                break
        except ValueError:
            print("error，Please enter an existing formula！")
    if(choice == -1):
        break
    formula = formulas[choice]
    params = []
    if formula['name'] == 'perimeter and area of triangle':
    	while True:
    	    for i in range(formula['params']):
    	        qaq = get_user_input(formula['prompt'],"Please enter a valid number!")
    	        params.append(qaq)
    	    if params[0] + params[1] > params[2] and params[0] + params[2] > params[1] and params[1] + params[2] > params[0]:
    	        break
    	    else:
                params = []
                print("Make sure these three sides form a triangle!")
            	
    else:
        for i in range(formula['params']):
            qaq = get_user_input(formula['prompt'],"Please enter a valid number!")
            params.append(qaq)
    qwq = formula['class'](*params)
    print("========================================")
    print("perimeter:", qwq.calculate_perimeter())
    print("area:", qwq.calculate_area())
    print("========================================")


