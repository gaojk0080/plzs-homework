import math

def calculate_square(side):
    per =  4 * side
    area = side * side
    return per, area


# 计算三角形面积
def calculate_triangle_area(base, height):
    return 0.5 * base * height

formulas = [
    {'name': '正方形周长及面积', 'func': calculate_square, 'params': 1, 'prompt': '请输入正方形的边长：'},
    {'name': '三角形面积', 'func': calculate_triangle_area, 'params': 2, 'prompt': '请依次输入三角形的底边长度和高：'}
]

while(1):
    print("可选的几何公式：")
    print(f"0. 退出")
    for i, formula in enumerate(formulas):
        print(f"{i+1}. {formula['name']}")
    while True:
        try:
            choice = int(input("请选择公式（输入对应编号）：")) - 1
            if(choice == -1):
                break
            if choice >1 or choice <-1:
                print("输入错误，请输入一个存在的公式！")
            else:
                break
        except ValueError:
            print("输入错误，请输入一个存在的公式！")
    if(choice == -1):
        break
    formula = formulas[choice]
    params = []
    for i in range(formula['params']):
        while True:
            try:
                qwq = float(input(formula['prompt']))
                if qwq <= 0:
                    print("输入错误，请重新输入合法的数！")
                else:
               	    params.append(qwq)
               	    break
            except ValueError:
                print("输入错误，请重新输入合法的数！")
                i = i - 1
                continue
    result = formula['func'](*params)
    print(f"计算结果：{result}")
