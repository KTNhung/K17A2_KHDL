def bai101():
    import math
    x = [1,2,3,4,5,6]
    print(max(x))
    print(min(x))


def bai102():
    import math
    x = int(input("Nhập số: "))
    print(math.fabs(x))


def bai103():
    import math 
    x = int(input("Nhập số: "))
    n = int(input("Nhập số: "))
    print((math.pow(x,2)+1)*n)


def bai104():
    import math
    x = int(input("Nhập số: "))
    n = int(input("Nhập số: "))
    print((math.pow(x,2)+ x + 1)*n + (math.pow(x,2)- x + 1)*n )

def bai105():
    x = input("Nhập chuỗi: ")
    if len(x) == 6:
        print("True") 
    else:
        print("False") 


def bai106():
    import math
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    c = int(input("Nhập c: "))
    if a == 0:
        if b == 0:
            if c  == 0:
                print("Vô số nghiệm")
            else:
                print("Vô nghiệm")
        elif b != 0: 
            x = -c/b
            print("Nghiệm của phương trình là: ", x)
    elif a != 0:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Vô nghiệm")
        elif delta == 0:
            x = -b/2*a
            print("Phương trình có nghiệm kép", x)
        elif delta > 0:
            x1 = ( -b + math.sqrt(delta))/2*a
            x2 = ( -b - math.sqrt(delta))/2*a
            print(f"Phương trình có 2 nghiệm là {x1} và {x2}")

def bai107():
    s = input("Nhập chuỗi s: ")
    s_sub = input("Nhập chuỗi con s_sub: ")
    s_find = input("Nhập chuỗi tìm s_find: ")
    s_replace = input("Nhập chuỗi thay thế S_replace: ")
    print("Chuỗi sau khi loại bỏ khoảng trắng ở đầu và cuối chuỗi: ", s.strip())
    print("Số lần chuỗi con s_sub xuất hiện trong chuỗi s: ", s.count(s_sub))
    print("Chuỗi s sau khi tìm kiếm và thay thế:", s.replace(s_find, s_replace))


def bai108():
    from datetime import datetime
    import calendar
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))
    now = datetime(nam,thang,ngay)
    print("Ngày tháng năm vừa nhập:", now.strftime("%d-%m-%Y"))

    nam_nhuan = calendar.monthrange(nam, 2)
    if nam_nhuan[1] == 29:
        print(f"Năm {nam} là năm nhuận.")
    else:
        print(f"Năm {nam} không là năm nhuận.")

    thu = calendar.weekday(nam,thang,ngay)
    if thu == 0:
        print(now.strftime("%d-%m-%Y"), "là thứ Hai")
    elif thu == 1:
        print(now.strftime("%d-%m-%Y"), "là thứ Ba")   
    elif thu == 2:
        print(now.strftime("%d-%m-%Y"), "là thứ Tư")   
    elif thu == 3:
        print(now.strftime("%d-%m-%Y"), "là thứ Năm")   
    elif thu == 4:
        print(now.strftime("%d-%m-%Y"), "là thứ Sáu")   
    elif thu == 5:
        print(now.strftime("%d-%m-%Y"), "là thứ Bảy")   
    elif thu == 6:
        print(now.strftime("%d-%m-%Y"), "là Chủ nhật")   

    print(f"Số ngày trong tháng {thang} là {calendar.monthrange(nam, thang)[1]}")

bai108()
    