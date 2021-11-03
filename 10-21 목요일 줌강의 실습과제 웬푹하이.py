### chapter 05

#cpe05-01

#cpe05-02
##a = int(input("a : "))
##b = int(input("b : "))
##c = a + b - b*b
##if c >= 0:
##    print(c)
##else :
##    print("음수")

#cpe05-03
##num = int(input("정수 : "))
##if  num % 2 == 0 and num % 3 == 0:
##    print("나누어짐")
##else:
##    print("나누어지지 않음")
#cpe05-04
##a = int(input("a :"))
##b = int(input("b :"))
##tmp = a - b
##if tmp > 0:
##    print("a > b")
##elif tmp < 0:
##    print("a < b")
##else:
##    print("a == b")

#cpe05-05
##a = 5
##b = 3
##ch = input("연산자 : ")
##if ch == "+":
##    tmp = a + b
##elif ch == "-":
##    tmp = a - b
##elif ch == "*":
##    tmp = a * b
##elif ch == "/":
##    tmp = a / b
##print(a,ch,b, "=", tmp)

#cpe05-06
##ph = int(input("pH :"))
##if ph >= 0  and ph <= 4:
##    print("강산성")
##elif ph = 5 and ph = 6:
##    print("약산성")
##elif ph = 7:
##    print("중성")
##elif ph = 8 and ph = 9:
##    print("약염기성")
##elif ph >= 10 anf ph <= 14:
##    print("기염기성")

#cpe05-07
##y = int(input("년도 : "))
##if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
##    print("윤년")
##else:
##    print("평년")

#cpe05-08
##h = int(input("키(cm) : "))
##w = int(input("몸무게(kg) : "))
##
##h *= 0.01


#cpe05-09
#cpe05-10
##opnd1 = int(input("피연산자1: "))
##if opnd1 >= 100 and opnd1 <= 999:
##
##    opnd2 = int(input("피연산자2: "))
##
##    if opnd2 >= 1 and opnd2 <= 9:
##          v3 = opnd1 // 100
##          v2 = opnd1 // 10 % 10
##          v1 = opnd1 % 10
##
##          print(opnd1, "*", opnd2)
##          print("=", "(", v3, "+", v2, "+", v1,")", "*", opnd2)
##          print("=", v3, "*", opnd2, "+", v2, "*", opnd2, "+", v1, "*", opnd2)
##          print("=", v3*opnd2, "+", v2*opnd2, "+",v1*opnd2)
##          print("=", opnd1* opnd2)
##    else:
##          print("onpd2 입력 오류")
##else:
##    print("onpd1 입력 오류")


#cpe05-11
import turtle as f
f.shape("tuetle")
a = int(input("반지름: "))
b = int(input("도형 종류: "))
c = int(input("바깔 원(1:0, 0:X): "))
#cpe05-12
direction = int(input("방향(완쪽: 1,오른쪽: 2,위쪽: 3,아래쪽: 4): "))
import turtle as f
f.shape("turtle")
if direction == 1:
    f.setheading(180)
elif direction == 2:
    f.setheading(0)
elif  direction == 3:
    f.setheading(90)
elif  direction == 4:
    f.setheading(-90)

          






