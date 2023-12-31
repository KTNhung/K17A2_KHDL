def bai111():
    a = [1,2,3]
    b = [1,[2,3]]
    c = []
    d = [1,2,3][1:]

    print(len(a))
    print(len(b))
    print(len(c))
    print(len(d))


def bai112():
    teams = [["Steven", "Neena", "Lex", "Alexandar", "Bruce"], ['David', 'Jack', 'Bill', 'Tom', 'Mike', 'Daniel'], 
             ['Alexander', 'Adam', "Pâym", 'Kevin', 'Sigal', 'Mike']]
    print(teams[-1][1])



def bai113():
    list = ["ant", "bear", "cat", "dog", "elephant", "fish", "goat", "hippo"]
    print("List of animals: ", list)
    print("Number of animals: ", len(list))
    find = input("I want to find: ")
    print(f"There is {find} in list of animals")



def bai114():
    a = []
    a.append(int(input("Nhập giá trị: ")))
    while True: 
        print("Tiếp tục nhập giá trị ? 1: Có, 0: không")
        n = int(input())
        if n == 1: 
             print(a.append(int(input("Nhập giá trị: "))))
        elif n == 0:
            break 
    x = int(input("Nhập giá trị cần tìm: "))
    print("List:", a)
    print("Tổng các giá trị trong list:", sum(a))
    print(x, "xuất hiện", a.count(x), 'trong list')

    if x >= max(a):
        print(x, "là số lớn nhất trong list")
    else:
        print(x, "khong phải số lớn nhất")
    b = []
    for i in (a):
        if x < i: 
            b.append(i)
    print(f"Các số lớn hơn {x} trong list: {b}")


def bai115():
    def list(a):
        print("Tiếp tục nhập giá trị? 1: Có, 0: Không")
        n = int(input())
        while True:
            if n == 1:
                a.append(int(input("Nhập giá trị: ")))
            if n == 0:
                break
    def songuyento(x):
        if x < 2: 
            return False
        for i in range(2,x):
            if x%i == 0:
                return False
        return True 
    a = []
    
    a.append(int(input("Nhập giá trị: ")))
    list(a)
    print("List: ", a)
    
    cacsonguyento = []
    for i in a:
        if songuyento(i):
            cacsonguyento.append(i)
    print("Các số nguyên tố trong list: ", cacsonguyento)

    am = []
    for i in a:
        if i < 0:
            am.append(i)
    print("Các phần tử âm trong list: ", am)
    print("Trung bình cộng các phần tử âm: ", sum(am)/len(am))
    
    duong = []
    for i in a:
        if i > 0:
            duong.append(i)
    print(f"Các phần tử dương trong list: {duong}")
    print(f"Trung bình cộng các phần tử dương: {sum(duong)/len(duong)}")

    print(f"Giá trị max trong list {max(a)}")
    print(f"Giá trị min trong {min(a)}")
    a.sort()
    print(f"List sắp tăng dần: {a}")


def bai116():
    list = [74,74,72,72,73,69,69,71,76,71]
    list_new = []
    for i in list:
        list_new.append(i/0.1)

    print(list_new[0:3])
    print(list_new[-3:])

    print(sum(list_new)/len(list_new))
    print(max(list_new))
    print(min(list_new))

    list_new.sort()
    print(list_new)

    list_new.reverse()
    print(list_new)


def bai117():
    def elementwise_greater_than(L, thresh):
        l = len(L)
        a = []
        for i in range(l):
            if L[i] <= thresh: 
                a.append(False)
            else:
                a.append(True)
        return a
    L = [1,2,3,4]
    thresh = int(input("Nhập "))
    b = elementwise_greater_than(L, thresh)
    print(b)


def bai118():
    def has_lucky_numbers(nums):
        for i in nums:
            if i%7:
                return True 
            else: 
                return False
    
    nums = [2, 6, 7, 9]
    print(has_lucky_numbers(nums))


def bai119():
    arrivals = ["Adela", "Fleda", "Owen", "May", "Mona", "Gilbert", "Ford"]
    def partty_late(a, name):
        t = len(a)/2
        c = a.index(name)
        if a[c] == a[-1]:
            return False 
        if c > t:
            return True
        else: 
            return False
    
    print(partty_late(arrivals, name = "May"))



def bai1110():
    meal_1 = ["a", "b", "c", "b", "d"]
    meal_2 = ["a", "b", "c", "d"]
    meal_3 = ["a", "b", "b", "b", "e"]
    def menu_is_boring(a):
        for i in range(len(a) - 1):
            if a[i] == a[i+1]:
                return True 
        return False
    print(menu_is_boring(meal_1))


def bai1111():
    tuple = ('Quỳnh Anh', 'Đạt', 'Chi', 'Quỳnh Anh', "Dương", 'Tú', 'Quý', 'Tú', 'Tuyết', 'Thư')
    while True:
        n = int(input("Nhập số từ 0 đến 9: "))
        if n < 0 or n > 9:
            print("Vui lòng nhập lại số từ 0 đến 9.")
        else:
            break
    while True: 
        m = int(input("Nhập số từ -1 đến -9: "))
        if m > -1 or m < -9:
            print("Vui lòng nhập lại số từ -1 đến -9.")
        else:
            break
    z = input("Nhập chuỗi cần tìm: ")
    
    print(f"Tuple[{n}] = {tuple[n]}")
    print(f"Tuple[{m}] = {tuple[m]}")
    print(z, "xuất hiện trong tuple", tuple.count(z), "lần")

import ham_list_11
def bai1112():
    tuplea = (1,3,2,4)
    tupleb = (5,8,6,7)
    tuplec = tuple(tuplea + tupleb)
    a = list(tuplec)
    ham_list_11.sapxep(a)
    tupled = tuple(a)
    print(f"Tuple d: {tupled}")
    print(f"Tuple[3] = {tupled[3]}")
    print(f"3 phần tử cuối cùng của tuple d {tupled[-3:]}")
    
bai1112()
