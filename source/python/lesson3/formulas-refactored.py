import math

def calculate_square(side):
    while(side<=0):
        side = float(input("应输入一个正数："))
    per =  4 * side
    area = side * side
    return per, area


# 计算三角形面积
def calculate_triangle_area(base, height):
    while base <= 0:
        base = float(input("应输入一个正数"))
    while height <= 0:
        height = float(input("应输入一个正数"))
    return 0.5 * base * height

formulas = [
    {'name': '正方形', 'func': calculate_square, 'params': 1, 'prompt': '请输入正方形的边长：'},
    {'name': '三角形', 'func': calculate_triangle_area, 'params': 2, 'prompt': '请输入三角形的底边长度和高：'}
]

print("可选的几何公式：")
for i, formula in enumerate(formulas):
    print(f"{i+1}. {formula['name']}")

choice = int(input("请选择公式（输入对应编号）：")) - 1
while choice >1 or choice <0:
    choice = int(input("请输入一个存在的公式：")) - 1
formula = formulas[choice]
params = []
for i in range(formula['params']):
    params.append(float(input(formula['prompt'])))

result = formula['func'](*params)
print(f"计算结果：{result}")
