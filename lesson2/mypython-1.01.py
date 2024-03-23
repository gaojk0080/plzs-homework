def Fibonacci_Sequence():
#{  
    qwq = 0;
    a = float(input("输入斐波纳契数列的最大值："));
    while(a<=0 or a%1 != 0):
    #{
        a = float(input("请输入一个正整数！重新输入："));
    #} 
    b = 0;
    c = 1;
    d = 1;
    qaq = 0;
    print(b, end=", ");
    print(c, end=", ");
    print(d, end=", ");
    while(b < a and c < a and d < a):
    #{ 
        if(qaq == 0):
        #{
            b = c + d;
            if(b > a):
            #{
                break;
            #}
            print(b, end=", ");
            qaq = 1;
            continue;
        #}
        if(qaq == 1):
        #{
            c = b + d;
            if(c > a):
            #{
                break;
            #}
            print(c, end=", ");
            
            qaq = 2;
            continue;
        #}
        if(qaq == 2):
        #{
            d = b + c;
            if(d > a):
            #{
                break;
            #}
            print(d, end=", ");
            qaq = 0;
            continue;
        #}
    #}    
    print();
#}

Fibonacci_Sequence();

