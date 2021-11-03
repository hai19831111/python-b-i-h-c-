## chapter 07: coding progranming

##cpb07-1
##def print_python():
##    print("파이썬")
##
##print_python()

##cpb07-2
##def welcom():
##    print("환영합니다")
##for i in range(1,4,1):
##    welcom()

##
##def welcom():
##    for i in range(3):
##        print("환영합니다")
##
##welcom()

##cpb07-3
##def welcome(name):
##    print("환영합니다",name,"님")
##
##name = input("이름 입력: ")
##welcome(name)

##cpb07-4
##def print_str(st,cnt):
##    for i in range(cnt):
##        print(st)
##
##st = input("문자열: ")
##cnt = int(input("반복횟수: "))
##print_str(st,cnt)

##cpb07-5
##def dispch(ch,n):
##    for i in range(n):
##        print(ch, end="")
##ch = input("문자 입력: ")
##n = int(input("반복횟수: "))
##dispch(ch,n)
##
#### 2way
##def dispch(ch,n):
##    for i in range(n):
##        print(ch*n)
##ch = input("문자 입력: ")
##n = int(input("반복횟수: "))
##dispch(ch,n)

##cpb07-6
##def maxnum(m,n):
##   if m > n:
##        print("큰 수 = ", m)
##   else:
##        print("큰 수 = ", n)
##
##m = int(input("숫자1: "))
##n = int(input("숫자2: "))
##maxnum(m,n)

##2way
def maxnum(m,n):
   if m > n:
        maxnum = m
   else:
        maxnum = n
   return maxnum

m = int(input("숫자1: "))
n = int(input("숫자2: "))
print("큰 수 = ", maxnum(m,n))
maxnum(m,n)

##cpb07-7
##def minnum(m,n):
##   if m < n:
##        print("작은 수 = ", m)
##   else:
##        print("작은 수 =  ", n)
##
##m = int(input("숫자1: "))
##n = int(input("숫자2: "))
##minnum(m,n)

##cpb07-8
##def pow_xy(x,y):
##    return x**y
##
##print("3 * 2**4 + 5 =", 3 * pow_xy(2,4) + 5)

##cpb07-9
##def rectangle_area(col,row):
##    core = col * row
##    print("가로",col,"세로",row, "인 사각형의 넓이 = ",core )
##col = int(input("가로: "))
##row = int(input("세로: "))
##rectangle_area(col,row)

##cpb07-10
##def circle_area(radius):
##    n = radius * radius * 3,141592
##    print("반지름", radius, "인 원의 넓이 =",n)
##    
##radius = int(input("반지름: "))
##circle_area(radius)
















