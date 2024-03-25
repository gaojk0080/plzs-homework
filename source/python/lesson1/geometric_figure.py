def Square():
    a = int(input("即将计算正方形周长与面积，请输入正方形边长："))
    print("正方形周长为", a * 4)
    print("正方形面积为", a ** 2)

def Triangle():
    a = int(input("即将计算三角形面积，请输入三角形底的长度:"))
    b = int(input("即将计算三角形面积，请输入对应的高的长度:"))
    print("三角形面积为", float(a * b / 2))


Square();
Triangle();




