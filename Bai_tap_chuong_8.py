#8.1
def bai81():
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    c = int(input("Nhập số c: "))
    d = int(input("Nhập số d: "))
    M = a
    m = a
    if M < b:
        M = b
    if M < c:
        M = c
    if M < d:
        M = d
    if m > b:
        m = b
    if m > c:
        m = c
    if m > d:
        m = d
    print("Số lớn nhất là:",M)
    print("Số bé nhất là:",m)


#8.2
def bai82():
    x = int(input("Nhập x: "))
    if x < 0:
        print("|x| =",-x)
    else:
        print("|x| =",x)


#8.3
def bai83():
    a = int(input("Hãy nhập a: "))
    b = int(input("Hãy nhập b: "))
    if a == 0: 
        if b == 0:
            print("Phương trình vô số nghiệm ")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = - b / a
        print("Phương trình có nghiệm là x =",x)


#8.4
def bai84():
    import math as m
    a = int(input("Cạnh a = "))
    b = int(input("Cạnh b = "))
    c = int(input("Cạnh c = "))
    p = (a + b + c)/2
    S = m.sqrt(p*(p - a)*p*(p - b)*p*(p - c))
    print("Diện tích tam giác là:", S)


#8.5
def bai85():
    n = int(input("Nhập Năm: "))
    if(n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
        print("Năm",n,"là năm nhuận")
    else:
        print("Năm",n,"không phải là năm nhuận")


#8.6
def bai86():
    t = int(input("Loại xe (4 hoặc 7): ")) 
    f = float(input("Số Km: ")) 
    w = int(input("Thời gian chờ (phút): ")) 
    pof = 0 
    pow = 0 

    if t == 4:
        if f < 0.8:
            pof = (f/0.8) * 11000
            f = f - 0.8
        elif f < 21:
            f = f - 0.8
            pof = pof + f*12100 + 0.8*11000
        else:
            f = f - 21
            pof = pof + f * 10000 + 20.2*12100 * 0.8*11000
        if t > 5:
            pow = (t - 5) * 800
    if t == 7:
        if f < 0.8:
            pof = (f/0.8) * 13000
            f = f - 0.8
        elif f < 21:
            f = f - 0.8
            pof = pof + f*14100 + 0.8*13000
        else:
            f = f - 21
            pof = pof + f * 12000 + 20.2*14100 * 0.8*13000
        if t > 5:
            pow = (t - 5) * 800
    print("Tiền chờ:",pow)
    print("Tiền di chuyển:",pof)
    print("Tiền cước:",pow + pof)
    

#8.7 
def bai87(): 
    e = float(input("Nhập số Kwh đã tiêu thụ: "))
    p = 0
    if e <= 50:
        p = p + 1.678*50
    elif e <= 100:
        p = 1.678*50
        e = e - 50
        p = p + 1.734*e
    elif e <= 200:
        p = p + 1.678*50
        e = e - 50
        p = p + 1.734*50
        e = e - 50
        p = p + 2.014*e
    elif e <= 300:
        p = p + 1.678*50
        e = e - 50
        p = p + 1.734*50
        e = e - 50
        p = p + 2.014*100
        e = e - 100
        p = p + 2.536*e
    elif e <= 400:
        p = p + 1.678*50
        e = e - 50
        p = p + 1.734*50
        e = e - 50
        p = p + 2.014*100
        e = e - 100
        p = p + 2.536*100
        e = e - 100
        p = p + 2.834*e
    else:
        p = p + 1.678*50
        e = e - 50
        p = p + 1.734*50
        e = e - 50
        p = p + 2.014*100
        e = e - 100
        p = p + 2.536*100
        e = e - 100
        p = p + 2.834*100
        e = e - 100
        p = p + 2.927*e
    print("Tổng số tiền:",p*1000,"đồng")


#8.8
def bai88():
    x = int(input("Nhập loại phòng: "))
    y = int(input("Nhập số đêm: "))
    if x == 1: 
        p = 1260000
    elif x == 2:
        p = 1550000
    elif x == 3 or x == 4:
        p = 1830000
    elif x == 5 or x == 6:
        p = 2120000
    elif x == 7: 
        p = 2540000
    elif x == 8:
        p = 4800000
    if y == 1:
        q = p
    elif y <= 3:
        q = p*75/100*y
    else:
        q = p*70/100*y
    print("Thành tiền:", q)


#8.9
def bai89():
    print("Input number: ")
    print("10")
    for i in range(10,0,-1):
        print(i)
    print("Start!!!")


#8.10
def bai810():
    n = int(input("Nhập n: "))
    x = float(input("Nhập x: "))
    print("S = (x*x + 1)^n = ", (int(x**2) + 1)**(n) )


#8.11
def bai811():
    n = int(input("Nhập n: "))
    x = float(input("Nhập x: "))
    print("A = ( x*x + x + 1 ) ^n + ( x*x - x + 1)^n =", (int(x**2) + int(x) + 1)**n + (int(x**2) - int(x) + 1)**n)


#8.12
def bai812():
    a = int(input("Nhập số: "))
    dem = 0 
    for i in range(2,a):
        if a%i == 0:
            dem = 1
            print("Đây khong phải số nguyên tố")
            break
    if a == 2:
        print("Đây là số nguyên tố")
    elif dem == 0:
        print("Đây là số nguyên tố")


#8.13
def bai813():
    n = int(input("Nhập số nguyên n: "))
    A = 0 
    B = 0
    C = 1
    D = 1
    E = 0 
    F = 0
    i = 0 
    for i in range(n + 1):
        if i%2 != 0:
            A += i
    print("A = ", A)

    for i in range(n + 1):
        if i%2 == 0:
            B += i
    print("B = ", B)

    for i in range( 1, n + 1 ):
        C *= i
    print("C = ", C)

    for i in range(1, n+1):
        if i%3 == 0:
            D *= i
    print("D = ", D)

    for i in range(2,n + 1):
        dem = 0
        for j in range(2, i):
            if i%j:
                dem = 1 
                break
        if dem == 0:
            E += i 
    print("E = ", E)

    for i in range(1, n + 1):
        if i % 2 == 0:
            F -= 1/i
        elif i % 2 != 0:
            F += 1/i
    print("F = ", F)
        

#8.14
def bai814():
    n = int(input("Số nguyên N = "))
    s = 0
    for i in range(n):
        print("Nhập số thứ",i+1)
        x = int(input())
        s += x
    print(s)


#8.15
def bai815():
    i = 0 
    S = 0
    while True : 
        x= int(input("Nhập một số nguyên (kết thúc là số 0 ): "))
        S += x 
        if x == 0:
            break
    print(S)


#8.16
def bai816():
    m = int(input("Nhập m = "))
    n = int(input("Nhập n = "))
    i = 0
    M = 0 
    while True: 
        i = i + 1
        if m % i == 0 and n % i == 0 and i > M: 
            M = i
        if i > m and i > n:
            break
    print(M)

#8.17
def bai816():
    m = int(input("Nhập m = "))
    n = int(input("Nhập n = "))
    BCNN = 0 
    while True:
        BCNN = BCNN + 1
        if BCNN % m == 0 and BCNN % n == 0:
            break
    print(BCNN)


#8.18
def bai818():
    x = int(input("Tui là số hoàn hảo: "))
    S = 0 
    for i in range(1, x):
        if x%i == 0: 
            print(i,"là ước của tui")
            S += i 
    if S == x:
        print("tui hoàn hảo")
    else:
        print("ròi tui sẽ hoàn hảo")
    
#8.19
def bai819():
    n = int(input("Nhập số đi "))
    S = ""
    print("Nhập", n,"số")
    for i in range(n):
        x = int(input("Nhập gì cũng được "))
        if x %2 != 0:
            S = str(x) + " " + S
    print(S)


#8.20
def bai820():
    x = int(input("Hãy nhập x: "))
    n = 1
    e = 1
    giaithua = 1
    while True:
        for i in range(1,n+1):
            giaithua = i*giaithua
        e = e + x**n/giaithua
        n += 1
        if x**n/giaithua < 10**(-4):
            break
    print(e)
bai820()



    
