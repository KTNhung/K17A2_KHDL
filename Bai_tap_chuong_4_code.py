#4.1 : HỆ PHƯƠNG TRÌNH BẬC NHẤT 
def bai41():    
    # a1x + b1y = c1
    # # a2x + b2y = c2

    a1 = int(input("a1: "))
    b1 = int(input("b1: "))
    c1 = int(input("c1: "))
    a2 = int(input("a2: "))
    b2 = int(input("b2: "))
    c2 = int(input("c2: "))

    if a1 / a2 == b1 / b2 and b1 / b2 == c1 / c2:
        print("HPT vô số nghiệm")
    elif a1 / a2 == b1 / b2 and b1 / b2 != c1 / c2:
        print("HPT vô nghiệm")
    else:
        x = (b2 * c1 - c2 * b1) / (a1 * b2 - a2 * b1)
        y = (c2 - a2 * x) / b2
        print(x,y)

#4.2 : TÌM UCLN
def bai42(): 
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


#4.3 TÍNH SỐ NGÀY CỦA MỘT THÁNG NĂM NÀO ĐÓ 
def bai43():
    m = int(input("Nhập tháng: "))
    n = int(input("Nhập năm: "))
    if m == 2:
        if (n % 4 == 0 and n % 100 != 0) or ( n % 4 ==0):
            d = 29
        else: 
            d = 28
    elif m < 8 and m % 2 != 0: 
        d = 31 
    elif m >= 8 and m % 2 == 0: 
        d = 31
    else: 
        d = 30 
    print("Số ngày của tháng", m,"năm", n, "là", d)

