#basic coding
#cpb-02
##subject = ['국어','영어','수학','과학','한국']
##for i in subject:
##    print(i, end=" ")

#cpb-03
##name = ["홍길동" ,"임꺽정"]
##subject = ['국어','영어','수학']
##for i in name:
##    for j in subject:
##        print(i,j)
##
###cpb-04

###cpb-05
##m = 0 #m= 홀수
##n = 0 #n= 짝수
##for i in range(1,101,1):
##    if i % 2 != 0:
##        m += i
##           
##    if i % 2 == 0:
##        n += i
##print("홀수: ", m)
##print("짝수: ", n)

#cpb-06
##s = 0
##for i in range(3,-4,-1):
##    print(i, end = " ")
##    s += i
##print("")
##print(s)

#cpb-07
##a = 1
##y = 0
##for i in range (1,11):
##    y += a/i
##    print(y)
   
#cpb-08
##y = 0
##for i in range(1,11,1):
##    y += i / (i + 1)
##    print(y)

#cpb-09
##y = 0
##sign = -1
##
##for i in range(1,11,1):
##    sign *= -1
##    y  += sign * 1/i
##    print(y)

#cpb-10
##n = int(input("단입력: "))
##if n >= 2 and n <= 9:
##    for i in range(1,10,1):
##        print(n," * ",i ,"=" ,n * i)

#cpb-11

#cpb-12
##for  i in range(1,6):
##    for j in range(1,5):
##        print("*", end = "")

#cpb-13
##for i in range(1,6):
##    for j in range(1,5):
##        print(i + j - 1, end = "")
##    print(" ")

### 13 2
##for i in range(1,6):
##    for j in range(i, i+3+1):
##        print(j,end="")
##    print(" ")

#cpb-14
##s = 0
##n = int(input("정수 입력: "))
##while n != 0:
##    s += n
##    n = int(input("정수 입력: "))
##    print("정수 : ", n)
##print("합: ", s)

#cpb-15
##pw = ""
##while pw != "pwpass":
##    pw = input("비밀번호: ")
##print("logIn Pass!!")

#cpb-16
##s = 0
##while True:
##    n = int(input("정수 입력: "))
##    if n < 0:
##        continue
##    if n == 0:
##        break
##    s += n
##print("합은: ", n)

#cpb-17
##import  turtle as f
##f.shape('turtle')
##radius = 50
##rotate = 120
##for i in range(int(360/rotate)):
##    f.circle(radius)
##    f.rt(rotate)

#cpb-18
##import  turtle as f
##f.shape('turtle')
##radius = 50
##rotate = 60
##for i in range(int(360/rotate)):
##    f.circle(radius)
##    f.rt(rotate)
    
#cpb-19
##import turtle as f
##f.shape('turtle')
##radius = 50
##for i in range(3):
##    f.down()
##    f.circle(radius)
##    f.up()
##    f.forward(radius)
##
###cpb-20
##f.clear()
##import turtle as f
##f.shape('turtle')
##radius = 50
##for i in range(3):
##    f.down()
##    f.circle(radius)
##    f.up()
##    f.forward(radius*2)



### enhancemen 1 coding programing ###

###pce-01
##maxnum = -sys, maxsize - 1
##minnum = -sys, maxsize
##
##num = [8, 7, 3, 9, 4, 1, 6, 5]
##for i in num:
##    if i > maxnum:
##        maxnum = i
##    if i < maxnum:
##        minnum = i
##print("최댓값: ", maxnum)
##print("최솟값: ", ,innum)
##
###for 문을 이용하지 않고 max(), min() 를 이용하여 리스트의 최댓값. 최숫값
##
##num = [8, 7, 3, 9, 4, 1, 6, 5]
##print("최댓값: ", maxnum)
##print("최솟값: ", ,innum)


### pce-03
#pce06-3
##for i in range(10,21):
##    f = i * 9/5 + 32
##    print(i,f)

#####pce-08
##for i in range(1,6):
##    for j in range(1,6-i):
##        print(" ", end="")
##    for j in range(1, i+1):
##        print("*", end="")
##    print(" ")

##pce-09
##for i in range(1,6):
##    for j in range(1,6-i):
##        print(" ", end="")
##    for j in range(1, i*2):
##        print("*", end="")
##    print(" ")


###cpe06-16 p171

radius= int(input("반지름: "))
cnt = int(input("횟수: "))
distance = int(input("이동: "))
import turtle as f
f.shape('turtle')
for i in range(cnt):
    f.down()
    f.circle(radius)
    f.up()
    f.forward(radius*distance)





    
