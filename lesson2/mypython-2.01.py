def is_prime(a):
#{
    if a <= 1:
	#{
        return False;
	#}
    for i in range(2, int(a**0.5) + 1):
	#{
        if a % i == 0:
		#{
            return False;
		#}
	#}
    return True;
#}


a = float(input("请输入一个正整数："));
while(a <= 0 or a%1 != 0):
#{
    a = int(input("输入个正整数好不好："));
#}
if is_prime(a):
#{
    print(a,"是一个质数");
#}
else:
#{
    print(a,"不是一个质数");
#}
