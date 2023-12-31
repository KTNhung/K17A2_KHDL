def bai1():
    try:
        a = int(input("Nhập độ dài cạnh a: "))
        b = int(input("Nhập độ dài cạnh b: "))
        c = int(input("Nhập độ dài cạnh c: "))
    except ValueError:
        print("a,b hoặc c không phải kiểu số.")
    if a <= 0 or b <= 0 or c <= 0:
        print("a,b hoặc c nhận giá trị không hợp lệ")
    elif a + b < c or a + c < b or b + c < a:
        print("không phù hợp điều kiện tồn tại tam giác")
    print("Hoàn thành xử lí ngoại lệ")

def bai2():
    a = []
    m = 1
    c = 0
    error = 0
    while True:
        try:
            n = int(input("Hãy nhập số dương (0: Hủy): "))
            error = 0
            if n == 0:
                break
            elif n < 0:
                print("Lỗi số âm!!!")
                error = 1
            if len(a) == 0 and error == 0:
                print("Thêm",n,"vào list")
                a.append(n)
            elif error == 0:
                if n == a[len(a)-1]:
                    m += 1
                else:
                    m = 1
                if error == 0 and m == 4:
                    m -= 1
                    print("Lỗi nhập lặp lại!!!")
                    error = 1
                if n % 2 == 0:
                    c += 1
                else:
                    c = 0
                if error == 0 and c == 5:
                    c -= 1
                    print("Lỗi nhập chẵn!!!")
                    error = 1
                if error == 0:
                    print("Thêm",n,"vào list")
                    a.append(n)
        except ValueError:
                print("Lỗi nhập số!!!")
    print(a)
        
