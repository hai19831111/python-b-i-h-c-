###7 thinking!, comment coding

#7.1.2
#7.1
##print("1234567")
##print("박춘숙")
##print("1234567")
##print("박춘숙")
##print("")
##for i in range(1,3,1):
##    print("1234567")
##    print("박춘숙")
##print("")
##
##def sn():
##    print("1234567")
##    print("박춘숙")
##for i in (1,3,1):
##    sn()
##
##print("")

#7.2
##def print19():
##    for i in range(1,10,1):
##        print(i,end=" ")
##    print("")
##
##print19()

#7.2.1

##def fadd(m,n):
##    s = n + m
##    print(n, "+", m, "=",s)
##a = 3
##b = 4
##fadd(a,b)

#program p07-02
##def calc_gugudan(dan):
##    if d >= 1 and d <= 9:
##        for i in range(1,10,1):
##            print(dan, "*", i, "=", dan*i)
##    else:
##        print("입력 단은 1~9까지 입력해주세요")
##        
##d = int(input("단 입력: "))
##calc_gugudan(d)

#comment coding 3
##def print19(st,ed):
##    for i in range(1,10,1):
##        print(st, "*", i, "=", st*i )
##    print("")
##
##s = int(input("시작 값:"))
##e = int(input("끝 값: "))
##if s < e:
##    print19(s,e)
##else :
##    print("시작 밦이 끝 값보다 작아야 합니다")

#7.2.2
##def fadd(n,m):
##    s = n + m
##    return s
##a = 3
##b = 4
##r = fadd(a,b)
##print("반환값= ", r)
##print("반환값= ", fadd(a,b))
##print(r + 2 + fadd(a,b))

#program p07-03
##
##def avg(a,b):
##    s = (a+b) / 2
##    return s
##in1 = int(input("값1= "))
##in2 = int(input("값2= "))
##r = avg(in1,in2)
##print("평균: ", r)

# coding 4

def avg(a,b,c):
    s = (a + b + c) / 3
    return s
in1 = int(input("값1= "))
in2 = int(input("값2= "))
in3 = int(input("값3= "))
r = avg(in1,in2,in3)

print("평균: ", r)
print("평균: ", avg(in1,in2,in3))


