### 20213086

###1
##clear = delete
##reset = 
###2
##one = int(input("첫번째 숫차: "))
##two = int(input("두번째 숫차: "))
##num = one + two
##print("정수1", one, "+", "정수2", two, "=", "합",num )

###3
##s = 0
##for i in range(1,10,2):
##    s += i
##    print(i,",", ":", s)

###4
##import turtle as f
##f.shape("turtle")
##f.setup(400,400)
##f.write(f.position())  ### 조건1
##f.forward(100)
##f.up()
##f.goto(0,-50)
##f.down()
##f.write(f.position())
##f.forward(100)
##f.up()
##f.goto(0,-100)
##f.down()
##f.write(f.position())
##f.forward(100)


#### 조건
##import turtle as f
##f.shape('turtle')
##f.setup(400,400)
##f.write(f.position())  ### 조건4
##f.forward(200)         ### 조건2
##f.up()
##f.goto(100,-50)         ### 조건2
##f.down()
##f.write(f.position())  ### 조건4
##f.forward(200)         ### 조건2
##f.up()
##f.goto(200,-100)         ### 조건2
##f.down()
##f.write(f.position())  ### 조건4
##f.forward(200)


###5
##name = str(input("이름은: "))
##ID = int(input("학번은: "))
##department = str(input("학과는: "))
##print("이름은 : ", "['",name,"']")
##print("학번은: ",  "['",ID,"학번","']")
##print("학과는: ", "['",department,"']")


###6
for i in range(1,6):
    for j in range(1,6-i):
        print(" ", end="")
    for j in range(1, i+1):
        print("*", end="")
    print(" ")

###7
score1 = int(input("필기점수: "))
score2 = int(input("실기점수: "))
if score1 >= 80 and score2 >= 70:
##    print("필기점수: ", score1)
##    print("실기점수: ", score2)
    print("합격입니다")
   
else:
     print("불합겹입니다")
    









