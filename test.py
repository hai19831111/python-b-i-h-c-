nhap = str(input("그리고 싶은 그림을 입력: ")) #nhahinhmuonve
import turtle as f
b = "삼각형" #amgiac
c = "정사각형" #hinhvuong
d = "직사각형" #chunha
while (nhap == b or nhap == c or nhap == d):
        nhap = str(input("그리고 싶은 그림을 입력: "))
        if nhap == "삼각형":
            nhap1 = int(input("측정 입력: ")) ##nhasodo
            f.clear()
            for i in range(3):
                f.forward(nhap1)
                f.lt(120)
            #f.clear()
        elif nhap == "정사각형":
            nhap2 = int(input("측정 입력: "))
            f.clear()
            for i in range(4):
                f.forward(nhap2)
                f.lt(90)
           # f.clear()
        elif nhap == "직사각형":
            nhap3 =  int(input("너비 측정 입력: "))#chi
            nhap4 =  int(input("길이 측정 입력: ")) #chieudai
            f.clear()
            for i in range(2):
                f.forward(nhap3)
                f.lt(90)
                f.forward(nhap4)
                f.lt(90)
           
