def Square():
#{
    a = float(input("即将计算正方形周长与面积，请输入正方形边长："));
    while(a<=0 or a%1 != 0):
    #{
        a = float(input("请输入一个正整数！重新输入："));
    #}
    print("正方形周长为", a * 4);
    print("正方形面积为", a ** 2);
#}

def Triangle():
#{
    a = float(input("即将计算三角形面积，请输入三角形底的长度:"));
    while(a <= 0 or a % 1 != 0):
    #{
        a = float(input("请输入一个正整数！重新输入："));
    #}
    b = float(input("即将计算三角形面积，请输入对应的高的长度:"));
    while(b<=0 or b%1 != 0):
    #{
        b = float(input("请输入一个正整数！重新输入："));
    #}

    print("三角形面积为", float(a * b / 2));
#}


def choose():
#{
    ch = int(input("请选择要计算的公式，1为正方形，2为三角形，3为退出:"));
    while(1):
	#{
        match(ch):
		#{
            case 1:
			#{
                Square();
                ch = int(input("请选择要计算的公式，1为正方形，2为三角形，3为退出:"));
			#}
            case 2:
			#{
                Triangle();
                ch = int(input("请选择要计算的公式，1为正方形，2为三角形，3为退出:"));
			#}
            case 3:
			#{
                break;
			#}
            case _:
			#{
                ch = float(input("请输入一个合法的数"));
			#}
		#}
	#}
#} 
choose();




