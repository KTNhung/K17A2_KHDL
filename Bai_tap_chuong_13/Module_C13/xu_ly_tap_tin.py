def read_file(filename):
    file = open(filename)
    a = file.read()
    print(a)
    

def read_report_file(filename):
    file = open(filename,"r")
    a = file.read()
    file.close()
    print("Content of file:\n")
    print(a)
    print("\n-----Report: Lines/Words/Chars-----")
    dong = a.split("\n")
    tu = []
    for i in range(len(dong)):
        tu += dong[i].split(" ")
    chu = len(a)
    print(f"\nLines: {len(dong)}, Words: {len(tu)}, Chars: {chu}")
    

def write_file(filename, content):
    file = open(filename,"w+")
    file.write(content)
    file.close()

def write_end_of_file(filename):
    file = open(filename,"a+")
    s1 = input("Hãy nhập nội dung cho tập tin: ")
    report = s1
    file.write(f"{s1}\n")
    while True:
        i = int(input("Có muốn nhập tiếp hông (1: Có, 0: Không): "))
        if i == 0:
            break
        s1 = input("Mời nhập tiếp: ")
        report += s1
        file.write(f"{s1}\n")
    file.close()
    print(f"Đã ghi nội dung vào {filename}:\n{report}")


import csv
def read_file_csv(filename):
    file = open(filename)
    a = []
    for i in csv.reader(file):
        a.append(i)
    for i in a:
        print(i)

def write_csv(filename,listContent):
    init = ["Name","Phone Number"]
    file = open(filename,'w')
    csv.writer(file).writerow(init)
    for row in listContent:
        csv.writer(file).writerow(row)

