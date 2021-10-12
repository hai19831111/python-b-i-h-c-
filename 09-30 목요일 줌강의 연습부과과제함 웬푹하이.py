### 20213086 웬푹하이
### 104-1
##홍길동의_나이= 5
##아버지의_나이= 38 - 홍길동의_나이 
##어머니의_나이= 34 - 홍길동의_나이
##print("아버지의_나이= ", 아버지의_나이 )
##print("어머니의_나이= ", 어머니의_나이)

### 104-2
##radius1 = int(input("반지름: "))
##py= float(3.141592)
##넓이 = radius1*py
##둘레 = 2*radius1*py
##print("원의 넓이 = ",  넓이)
##print("원의 둘레 =", 둘레)

### 104-3
##s1 = int(input("웟변: "))
##s2 = int(input("밑변: "))
##s3 = int(input("높이: "))
##s4 = (s1 + s2) * s3 / 2
##print("사다리꼴의 넓이: ", s4)

### 104-4
##s1 = int(input("분: "))
##s2 = 60
##s3 = s1 * s2
##print(s3 ,"초")


### 105-5
##t = int(input("초: "))
##minute = (t // 60) % 60
##second = (t%60) % 60
##
##print(t, "초", "=", minute, "분", second, "초")

### 105-6
##t = int(input("초: "))
##m = 3.4
##s1 = int(t * m)
##print(s1, "m")

### 105-7
##s1 = float(input("1초당 움직이는 거리: "))
##s2 = s1 * (60 * 60)
##s3 = s2 / 1000
##print("시속 : ", s2,"m/h")
##print("시속 : ", s3, "km/h")

### 105-8
##t = int(input("섭씨온도: "))
##v = 331 + 0.6 * t
##print("음속 ; ", v, "m/s")                    # ch lam

### 106-9
##inch = int(input("인치: "))
##Cm = float(inch * 2.54)
##print(inch, "인치", "=", Cm, "센티미터" )

### 106-10
##cm = int(input("센티미터: "))
##inch = float(cm * 0.39370)
##print(cm, "센티미터", "=", inch, "인치" )

### 106-11
##s1 = int(input("닭: "))
##s2 = int(input("토끼: "))
##s3 = int(input("돼지: "))
##pesi = (s1*2)+(s2*4)+(s3*4)
##print("다리 합계: ", pesi)

### 106-12
##year = int(input("경과 연수: "))
##tabacco = float(4.500)
##yyear = 365 * tabacco
##year_year = year * yyear *tabacco
##print("1 년 총지출: ", yyear, "원")
##print(year, "년 총지출",year_year, "원")

### 107-13
##s1 = int(input("피연산자1: "))
##s2 = int(input("피연산자2: "))
##print(s1,"+",s2)
##print("= (",s1//100,"+",s1//10%10,"+",s1%10,") *", s2)
##print("=", s1//100,"*",s2,"+",s1//10%10,"*",s2,"+",s1%10,"*",s2)
##print("=", s1//100 * s2,"+", s1//10%10*s2, "+", s1%10 * s2)
##print("=", s1 * s2)


### 107-14
##a = int(input("lenght: "))
##b = int(input("distance: "))
##import turtle as f
##f.shape('turtle')
##f.speed(1)
##f.forward(a)
##f.penup()
##f.goto(0,-(b*1))
##f.pendown()
##f.forward(a)
##f.penup()
##f.goto(0,-(b*2))
##f.pendown()
##f.forward(a)

### 108-15
a = int(input("lenght: "))
b = int(input("distance: "))
import turtle as f
f.shape('turtle')
f.speed(1)
f.forward(a+b*0)
f.penup()
f.goto(0,-(b*1))
f.pendown()
f.forward(a+b*1)
f.penup()
f.goto(0,-(b*2))
f.pendown()
f.forward(a+b*2)

### 108-16
##a = int(input("radius: "))
##import turtle as f
##f.shape('turtle')
##f.speed(1)
##f.circle(a)
##f.penup()
##f.goto(0,a*2)
##f.pendown()
##f.circle(a/2)

















