### 9.1
## 1) 키 조작 관련(p254-256)
##import turtle as t
##
##def print_key(char):
##    print(char, end="")
##
##def key_a():
##    print_key("a")
##
##def key_sp():
##    print_key("s_")
##
##def key_sr():
##    print_key("s^")
##
##s = t.Screen()
##s.onkey(key_a, "a")
##s.onkeypress(key_sp, "s")
##s.onkeyrelease(key_sr, "s")
##s.onkey(s.bye, "q")
##s.listen()

## 2
#2.1
##gv = 3

##def func1():
##    global gv
##    lv1 = 1
##    lv1 += gv
##    gv = gv + 1
##    print(lv1)
##    print(gv)
##
##def func2(pv):
##    lv2 = pv
##    print(lv2)
###main
##gv = 3
##func1()
##func2(2)
##print(gv)


#2.2
##gv = 3
##
##def func1():
##    lv1 = 1
##    gv = 1
##    lv1 += gv
##    print(lv1)
##    
##def func2(pv):
##    lv2 = pv
##    print(lv2)
###main
##
##func1()
##func2(2)
##print(gv)


#2.3
##gv = 3
##
##def func1():
##    lv1 = 1
##    gv = 1
##    lv1 += gv
##    print(lv1)
##
##def func2(pv):
##    lv2 = pv
##    print(lv2)
###main
##func1()
##func2(2)
##print(gv)


#2.4
##gv = 3
##
##def func1():
##    global gv
##    lv1 = 1
##    lv1 += gv
##    gv = 1
##    print(lv1, gv)
##
##def func2(pv):
##    lv2 = pv
##    print(lv2)
###main
##func1()
##func2(2)
##print(gv)

## comment coding 1 p256

##import turtle as t
##
##def print_digit(n):
##    print(n,end="")
##def key_1():
##    print_digit(1)
##def key_2():
##    print_digit(2)
##def key_3():
##    print_digit(3)
##
##s = t.Screen()
##s.onkey(key_1, "1")
##s.onkey(key_2, "2")
##s.onkey(key_3, "3")
##s.listen()


## comment coding 2 p260

##a = 1
##def func(d):
##    global a
##    b = a + 2
##    c = b + d
##    print("func: ", a,b,c,d)
##    a = c
##    print("func: ", a,b,c,d)
##    return c
##print("main: ", a)
##e = func(3)
##print("main: ", a,e)

## programing p09-01(p247-253)
import turtle as f

color_status = ["white", "blue", "red"]
alert_status = ["정상", "주의", "화재"]
tempc = 50

def check_fire():
    if tempc < 80:
        status = 0
    elif tempc < 120:
        status = 1
    else:
        status = 2

    f.clear()
    f.home()
    f.down()
    f.fillcolor(color_status[status])
    f.begin_fill()
    f.circle(20)
    f.end_fill()
    f.up()
    f.goto(-22,50)
    f.write("%s : %d"%(alert_status[status],tempc))

def keyUp():
    global tempc
    if tempc < 80:
        tempc += 5
    else:
        tempc += 10
    check_fire()

def keyDown():
    global tempc
    if tempc < 80:
        tempc -= 5
    else:
        tempc -= 10
    check_fire()

f.setup(300, 300)
s = f.Screen()
f.hideturtle()
f.speed(0)
check_fire()
s.onkey(keyUp, "up")
s.onkey(keyDown, "down")
s.onkey(s.bye, "q")
s.listen()


























