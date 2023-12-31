def bai91():
    def sign(x):
        if x < 0:
            return -1
        elif x > 0:
            return 1
        else:
            return 0
    print(sign(8))
    print(sign(-8))
    print(sign(0))


def bai92():
    def tinh_can(n):
        if n % 10 == 0: 
            return "Canh"
        elif n % 10 == 1:
            return "Tân"
        elif n % 10 == 2:
            return "Nhâm"
        elif n % 10 == 3: 
            return "Quý"
        elif n % 10 == 4:
            return "Giáp"
        elif n % 10 == 5: 
            return "Ất"
        elif n % 10 == 6: 
            return "Bính"
        elif n % 10 == 7:
            return "Đinh"
        elif n % 10 == 8:
            return "Mâu"
        elif n % 10 == 9: 
            return "Kỷ"
        
    def tinh_chi(n):
        if n % 12 == 0:
            return "Thân"
        elif n % 12 == 1:
            return "Dậu"
        elif n % 12 == 2:
            return "Tuất"
        elif n % 12 == 3:
            return "Hợi"
        elif n % 12 == 4:
            return "Tý"
        elif n % 12 == 5:
            return "Sửu"
        elif n % 12 == 6:
            return "Dần"
        elif n % 12 == 7:
            return "Mão"
        elif n % 12 == 8:
            return "Thìn"
        elif n % 12 == 9:
            return "Tỵ"
        elif n % 12 == 10:
            return "Ngọ"
        elif n % 12 == 11:
            return "Mùi"
        
    x = int(input("Nhập năm: "))
    print("Năm", x, "lịch âm là năm", tinh_can(x),tinh_chi(x) )



def bai93():
    def BMI(can_nang, chieu_cao):
        return can_nang/(chieu_cao * chieu_cao)

    a = float(input("Nhập cân nặng(kg):" ))
    b = float(input("Nhập chiều cao(m): "))
    print("Chỉ số bmi là: ", BMI(a,b))

    if BMI(a,b) < 18.5:
        print("Gầy") 
    elif BMI(a,b) < 25:
        print("Bình thường") 
    else:
        print("Thừa cân") 
    

def bai94():
    def S(n, x):
        S = ( x**2 + 1 )**n
        return S
    n = int(input("nhập số n: "))
    x = int(input("Nhập số x: "))
    print(S(n, x))


def bai95():
    def A(n, x):
        A = ( x **2 + x + 1)**n + (x**2 - x + 1)**n
        return A
    n = float(input("Nhập số n: "))
    x = float(input("Nhập số x: "))
    print(A(n,x ))

def bai96():
    def songuyento(x):
        if x == 2:
            return True
        elif x == 1:
            return False
        for i in range(2,x):
            if x % i == 0:
                return False
        return True

    x = int(input("Nhập số: "))
    print(songuyento(x))

bai96()

def bai97():
    def phan_nguyen(a, b):
        c = a // b 
        
        return c
    a = int(input("Nhập a:"))
    b = int(input("Nhập b: "))
    print(phan_nguyen(a, b))


def bai98():
    def sohoanhao(x):
        i = 0 
        S = 0
        for i in range(1, x):
            if x % i == 0:
                S += i 
        return S
    x = int(input("Nhập số đi: "))
    if sohoanhao(x) == x:
        print(sohoanhao(x), "là số hoàn hảo")

    else:
        print(sohoanhao(x), "khong phải số hoàn hảo")


def bai99():
    S_tron = lambda r: 3.14*r*r 
    P_tron = lambda r: 2*3.14*r
    S_hinhchunhat = lambda a, b: a*b
    P_hinhchunhat = lambda a, b: (a+b)*2
    r = int(input("Nhập bán kính hình tròn: "))
    a = int(input("Nhập chiều dài hình chữ nhật: "))
    b = int(input("Nhập chiều rộng hình chữ nhật: "))
    print("Diện tích và chu vi hình tròn là: ", S_tron(r), "và", P_tron(r))

