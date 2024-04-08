def convert_to_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while n > 0:
        n, remainder = divmod(n, base)
        result = digits[remainder] + result
    return result

def main():
    while True:
        try:
            user_input = int(input("请输入一个自然数："))
            if user_input <= 0:
                print("输入错误，请重新输入自然数！")
            else:
                break
        except ValueError:
            print("输入错误，请重新输入自然数！")
    for base in range(2, 37):
        converted_num = convert_to_base(user_input, base)
        print(f"{user_input}的{base}进制表示为：{converted_num}")

main()
