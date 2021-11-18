### cpe 08-03

##engkor_dict = dict()
##while True:
##    eng = input("영어 단어: ")
##    kor = input("한글 단어: ")


### cpe 08-04
##engkor_dict = dict()
##while True:
##    eng = input("영어 단어: ")
##    if eng == "":
##        break
##    if len(engkor_dict) > 0:
##        if eng in engkor_dict:
##            print(eng,":", engkor_dict[eng])
##            continue
##        else:
##            print(eng,"단어가 등록되어 있디 않습니다.")
##
##    else :
##        print("사전이 비어 있습니다. ")
##    print("단어를 추가합니다.")
##    kor = input("한글 단어: ")
##
##    engkor_dict[eng] = kor
##print(engkor_dict)

### cpe 08-05
##moneys = {1:50000, 2:10000, 3:5000, 4:1000, 5:500, 6:100, 7:50, 8:10, 9:5, 10:1}
##price = int(input("금액: "))
##p = price
##un = 0 #화폐단위의 사용종류
##tn = 0 #총 화폐 사용 갯수
##for i in moneys:
##    tmp = p // moneys[i] #몫
##    if tmp >= 1:
##        un = un + 1
##    tn = tn + tmp
##    print(moneys[i], ":", tmp)
##    p = p % moneys[i] #나머지
##    
##print("총", un, "종류", tn,"개 필요")



### cpe 08-06
##import math
##from math import trunc
##
##
##moneys = {1:50000, 2:10000, 3:5000, 4:1000, 5:500, 6:100, 7:50, 8:10, 9:5, 10:1}
##price = int(input("금액: "))
##p = price
##un = 0 #화폐단위의 사용종류
##tn = 0 #총 화폐 사용 갯수
##for i in moneys:
###   tmp = p // moneys[i] #몫
##    tmp = trunc(p / moneys[i])
##    if tmp >= 1:
##        un = un + 1
##    tn = tn + tmp
##    print(moneys[i], ":", tmp)
###    p = p % moneys[i] #나머지
##    p = p - tmp * moneys[i]
##    
##print("총", un, "종류", tn,"개 필요")

### cpe 08-07
##import math
##import turtle as t
##
##t.setup(300,300)
##s = t.Screen()
##t.speed(10)
##basex = 0
##basey = 0
##r = 100
##
##for a in range (0,361,1):
##    rad = math.radians(a)
##    x = basex + math.cos(rad)
##    y = basey + math.sin(rad)
##    t.up()
##    t.goto(x,y)
##    t.down()
##    t.dot(2)

### cpe 08-08
##import math
##import turtle as t
##
##t.setup(300,300)
##s = t.Screen()
##t.speed(10)
##basex = 0
##basey = 0
##r = 100
##
##for a in range (0,361,1):
##    rad = math.radians(a)
###   x = basex + math.cos(rad)
##    x = basex + math.cos(rad)
###   y = basey + math.sin(rad)
##    y = basey + math.sin(rad)
###   t.up()
##    t.goto(x,y)
##    t.down()
###    t.dot(2)

#cpe08-10
import turtle as t

def write_xy(x,y):
    t.goto(x,y)
    if x >= -100 and x <= 100 and y >= -100 and y <= 100:
        
        t.down()
        t.circle(20)
        t.up()
    else :
        t.write("x: %d, y : %d" %(x,y))

def screen_clear(x,y):
    t.goto(x,y)
    t.clear()

t.setup(600,300)
s = t.Screen()
t.up()

s.onscreenclick(write_xy, 1)
s.onscreenclick(screen_clear,1)


#cpb08-09






















