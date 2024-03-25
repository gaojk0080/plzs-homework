def printf_fib(f):
    a = 0
    while a < len(f) - 1:
        print(f[a], end=" / ")
        print(f[a+1], end=" = ")
        print(f[a] / f[a+1])
        a += 1

def generate_fibonacci(n):
    if n <= 1:
        return [0]
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fibonacci.pop()
    printf_fib(fibonacci)

a = int(input("请输入斐波那契数列的最大值："))
while(a<=1):
    a = int(input("请输入一个大于1的正整数："))
generate_fibonacci(a)
