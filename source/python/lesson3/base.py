def convert_to_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while n > 0:
        n, remainder = divmod(n, base)
        result = digits[remainder] + result
    return result

def main():
    a = int(input("请输入一个自然数："))
    while a <= 0:
        a = int(input("请输入一个自然数："))
    for base in range(2, 37):
        converted_num = convert_to_base(a, base)
        print(f"{a}的{base}进制表示为：{converted_num}")

main()
