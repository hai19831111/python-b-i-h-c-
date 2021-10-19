nhap = str(input("nhap_hinh_muon-ve: "))
import turtle as f
b = "tam giac"
c = "hinh vuong"
d = "hinh chu nhat"
while (nhap == b or nhap == c or nhap == d):
        nhap = str(input("nhap_hinh_muon-ve: "))
        if nhap == "tam giac":
            nhap1 = int(input("nhap so do: "))
            for i in range(3):
                f.forward(nhap1)
                f.lt(120)
        elif nhap == "hinh vuong":
            nhap2 = int(input("nhap so do: "))
            for i in range(4):
                f.forward(nhap2)
                f.lt(90)
        elif nhap == "hinh chu nhat":
            nhap3 =  int(input("nhap so do chieu rong: "))
            nhap4 =  int(input("nhap so do chieu dai: "))
            for i in range(2):
                f.forward(nhap3)
                f.lt(90)
                f.forward(nhap4)
                f.lt(90)
