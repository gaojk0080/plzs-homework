def fibonacci(n):
    fib_list = [0, 1]
    while fib_list[-1] <= n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:-1]

num = int(input("请输入一个正整数："))

fibonacci_sequence = fibonacci(num)

print("不超过{}的斐波那契数列为：".format(num))
for num in fibonacci_sequence:
    print(num, end=" ")
