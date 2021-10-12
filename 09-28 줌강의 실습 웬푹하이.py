##x = input("숫자1 입력: ")
##y = input("숫자2 입력: ")
##print(x, y)
##print(x+ y)
##
##
##x = int(input("숫자1 입력: "))
##y = int(input("숫자2 입력: "))
##print(x, y)
##print(x+ y)
##
##
##x = int(input("숫자1 입력: "))
##y = float(input("숫자2 입력: "))
##print(x, y)
##print(x+ y)

#program 04-01
##x = int(input("숫자1 입력: "))
##y = int(input("숫자2 입력: "))
##print(x+ y)
##print(x- y)
##print(x* y)
##print(x/ y)
##print(x// y)
##print(x% y)
##print(x+y/ 0)

## moment coding 1
##odd = 1 +3 +5 +7 +9
##even = 2 +4 +6 +8 +10
##diff = even - odd
##print(odd, even, diff)
##print("홀수의: ", odd, "짝수의 합: ", even, "홀짝의 차이:" ,diff)

## moment coding 2
##name =input("이름 입력: ")
##year =  int(input("출생연도 입력: "))
##age = 2021 -year + 1
##print("이름은", name, "나이는",age,"살입니다")

#program 04-02
##x = int(input("금액 입력: "))
##x500 = x // 500
##x100 = x % 500
##x100 = x100 // 100
##
##print("500원 동전의 갯수는" ,x500, "개 이고", "100원의동전의 갯수는 ",x100,"입니다.")
##print("500원 동전의 갯수는" ,str(x500)+ "개 이고", "100원의 동전의 갯수는 ",str(x100)+"입니다.")





#moment coding 3 67770입력 받이서 500원, 100원, 50원, 10원 동전의 갯수를 각각 출력하세요
x = int(input("금액 입력: "))
x500 = x // 500

x100 = x % 500
x100 = x100 // 100     ##exercise

x50 = x % 100
x50 = x50 // 50

x10 = x % 50
x10 = x10 // 10
print("x500:",x500,   "x100:",x100,  "x50:",x50,  "x10:",x10,"입니다")






#대입문 p89

##a = 1
##b = 1
##c = 1
##print(a,b,c)
##
##a=b=c=2
##print(a,b,c)
##
##x = int(input("정수1 입력: "))
##y = int(input("정수2 입력: "))
##print(x,y)
##
###x,y 값 치환
##z = x
##x = y
##y = z
##print(x,y)
##
##x,y = y,x
##print(x,y)
##
##a,b,c = 1,2,3
####a,b = 1,2,3 #failed
####a,b,c = 1,2 #failed
##
######증분 대입연산자자 p90
###x=1
##x=x+1 #x+=1
##x=x-1 #x-=1


####프로그램 04-03
##x= int(input("x 값 입력: "))
##print(x)
##
##x += 2
##print(x)
##
##x -= 2
##print(x)
##
##x *= 2
##print(x)
##
##x /= 2
##print(x)

# moment coding 4
##a=1
##b=2
##c=3
##a+=b
##b+=a-c
##c=a*(a-b)
##print(a,b,c)

## program 04-04
##x = int(input("정수1 입력:"))
##y = int(input("정수2 입력:"))
##
##z = (x+y)/2
##print("평균 : ", z)

## moment coding 5: (10,20,30,40,50)의 평균값을 a변수

##a = (10+20+30+40+50)/5
##print("평균값을 : ", a)
##
#### moment coding 6 : 3+2*4/2 를 계산하여 b변수
##b = 3+2*4/2
####              : 3+((2*4)/2) 를 계산하여 c변수
##c = 3+((2*4)/2)
##  
#### moment coding 7 : ((3+2)*4)/2 를 계산하여 d변수
##d = ((3+2)*4)/2
##
##print(a, b, c, d)







