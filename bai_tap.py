#1.1
print("**  ** ******    **      **     *******")
print("**  ** **        **      **     **   **")
print("****** ******    **      **     **   **")
print("**  ** **        **      **     **   **")
print("**  ** ** ****   ******  ******  ******")

#1.3 
so_luong = 5
don_gia = 25000
print("Tên hàng: Sữa hộp Vina Milk")
print("Số lượng:", so_luong)
print("Đơn giá:", don_gia)
print("Tiền phải trả:", so_luong * don_gia)

#1.4
a = float(input("Nhập a ="))
b = float(input("Nhập b ="))
c = float(input("Nhập c ="))
p = (a + b + c)/2
import math
print("Diện tích tam giác có số đo", a, b, c, "là :", math.sqrt(p*(p-a)*(p-b)*(p-c)))

import math
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Diện tích tam giác là:", s)