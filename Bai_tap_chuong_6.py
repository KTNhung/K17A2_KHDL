#1.1
print("**  ** ******    **      **     *******")
print("**  ** **        **      **     **   **")
print("****** ******    **      **     **   **")
print("**  ** **        **      **     **   **")
print("**  ** ** ****   ******  ******  ******")


#1.2
x = 10 
y = 5
print("x =",x, "y =",y)
print("Tổng x + y =", x + y )
print("Hiệu x - y =", x - y)
print("Tích x*y = ", x*y )
print("Thương x/y = ", x/y )

#1.3
so_luong = 5
don_gia = 25000
print("Tên hàng: Sữa hộp Vina Milk")
print("Số lượng:", so_luong)
print("Đơn giá:", don_gia)
print("Tiền phải trả:", so_luong * don_gia)


#1.4
a = (5-3)//2
b=(8-3)*(2-(1+1))
print(a)
print(b)


#1.5
x = int(input("Nhập số lượng: "))
y = int(input("Nhập đơn giá: "))
print("Thành tiền =", x*y)

#1.6
a = int(input("Alice_candies = "))
b = int(input("Bob_candies = "))
c = int(input("Carol_candies = "))
print("Số kẹo bị dư ra cần đập vỡ = ", (a + b + c)%3)

#1.7
c = float(input("Nhập độ C: "))
print("Nhiệt độ F là: ", 9/5*c + 32)

#1.8
x = input("Nhập chuỗi s1: ")
y = input("Nhập chuỗi s2: ")
z = input("Nhập chuỗi s3: ")
t = input("Nhập index: ")
print("Chiều dài chuỗi s1 =", len(x))
print("Chiều dài chuỗi s2 =", len(y))
print("Chiều dài chuỗi s3 =", len(z))
print("Chuỗi 4 =", x[2:5])
print("Chuỗi s2 lặp lại 2 lần =", y*2)


#1.9
x = float(input("Lãi suất 1 năm ( % ): "))
y = int(input("SỐ tiền gửi: "))
z = int(input("Số tháng gửi: "))
t = (z*y)*(x/100/12)
print("Tiền lãi = ", t, "vnd")
print("Tiền vốn + lãi = ", y, "+", t, "=", y + t, "vnd" )

