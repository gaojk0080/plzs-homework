#!/usr/bin/python3
def fibonacci_generator(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

def get_user_input():
    while True:
        try:
            user_input = int(input("请输入一个正整数："))
            if user_input <= 0:
                print("输入错误，请重新输入正整数！")
            else:
                return user_input
        except ValueError:
            print("输入错误，请重新输入正整数！")


user_input = get_user_input()
fib_gen = fibonacci_generator(user_input)
for num in fib_gen:
    print(num)

