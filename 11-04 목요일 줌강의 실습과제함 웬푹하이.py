###chater 8 basic python coding
#cpb08-1

##str = input("문자열 입력: ")
##print("문자열 길이 : ", len(str))
##print("첫 번째 문자: ", str[0])
##print("두 번째 문자: ", str[1])
##print("마지막 문자 : ", str[len(str)-1])

#cpb08-2

##str = input("문자열 입력: ")
##print("개별 문자 출력: ", end= "")
##
##for i in range(0 , len(str),1):
##    print(str[i], end= "")
##print("")
##
##print("역순 개별 문자 출력: ", end= "")
##for i in range(len(str)-1,-1,-1):
##    print(str[i], end= "")
##print("")

#cpb08-3

##score = int(input("점수: "))
##if score >= 0 and score <= 100:
##    if score >= 90:
##        degree = "A"
##    elif score >= 80:
##        degree = "B"
##    elif score >= 70:
##        degree = "C"
##    elif score >= 60:
##        degree = "D"
##    else :
##        degree = "F"
##    print(score , ":", degree)
##else :
##    print("입력 가능한 점수 범위는 0~100입니다")
    
#cpb08-4

##deg = {10:'A',9:'A',8:'B',7:'C',6:'D',5:'F',4:'F',3:'F',2:'F',1:'F'}
##score = int(input("점수: "))
##if score >= 0 and score <= 100:
##     sco = score // 10
##     degree = deg[sco]
##     print(score , ":", degree)
##else :
##    print("입력 가능한 점수 범위는 0~100입니다")

#cpb08-5

##items = {"라면": 650, "우유":1100, "콜라":1200, "과자":700, "캔커피":500}
##s = 0
##while True:
##    it = input("제품염: ")
##    if it == "":
##        break
##    if it in items :
##        s = s + items[it]
##        print("[%s:%d] > %d"%(it, items[it],s))
##    else:
##        print(it, "는 미등록 제품입니다")
##print("총금 액: ", s)

#cpb08-6

##import time as t
##for i in range(1,6,1):
##    print(i, end= " ")
##    t.sleep(2)
    
#cpb08-7

import math
num = float(input("실수 :"))
print(num, ":", math.cei(num))
print(num, ":", math.floor(num))
print(num, ":", math.trunc(num))

#cpb08-8
from math import sqrt
num = float(input("실수 :"))
print(num, ":", sqrt(num))


