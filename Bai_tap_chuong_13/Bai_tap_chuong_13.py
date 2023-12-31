from Module_C13 import xu_ly_tap_tin
def bai1():
    a = input("Nhập tên tập tin: ")
    xu_ly_tap_tin.read_file(a)


def bai2():
    a = input("Nhập tên tập tin: ")
    xu_ly_tap_tin.read_report_file(a)


def bai3():
    a = input("Nhập tên tập tin: ")
    b = input("Nhập nội dung tin: ")
    xu_ly_tap_tin.write_file(a, b)
    xu_ly_tap_tin.read_file(a)


def bai4():
    a = input("Nhập tên tập tin: ")
    xu_ly_tap_tin.write_end_of_file(a)
    xu_ly_tap_tin.read_file(a)


def bai5():
    a = input("Nhập tên tập tin: ")
    xu_ly_tap_tin.read_file_csv(a)


def bai6():
    a = input("Nhập tên tập tin: ")
    danh_ba = []
    while True:
        i = int(input("Nhập Tên Và Số Điện Thoại? (0: Không, 1: Có): "))
        if i == 0:
            break
        ten = input("Nhập tên: ")
        sdt = input("Nhập số điện thoại: ")
        danh_ba.append([ten,sdt])
    xu_ly_tap_tin.write_csv(a, danh_ba)
    xu_ly_tap_tin.read_file_csv(a)

