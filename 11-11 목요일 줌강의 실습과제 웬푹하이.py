# cpb08-10
##import turtle as f
##
##def write_xy(x,y):
##    if x >= -100 and x <= 100 and y >= -100 and y <= 100:
##        f.goto(x,y)
##        f.pendown()
##        f.circle(20)
##        f.penup()
##    else:
##        f.goto(x,y)
##        f.write("x:%d, y=%d 내에서 클릭하서야 합니다."%(x,y))
##    
##def screen_clear(x,y):
##    f.goto(x,y)
##    f.clear()
##    
##f.setup(600,300)
##s = f.Screen()
##f.penup()
##
##s.onscreenclick(write_xy, 1)
##s.onscreenclick(screen_clear, 3)

# cpb08-09

##def write_xyleft(x,y)
##    t.goto(x,y)
##    t.write("x:%d, y:%d - 마우스 왼쪽버튼 클릭")
##
##def write_xyright(x,y)
##    t.goto(x,y)
##    t.write("x:%d, y:%d - 마우스 오른쪽버튼 클릭")


# Chapter 08: coding? Programing!!!

# cpb08-1
# cpb08-2
items = {'공책': 325, '연필':427,  '지우개':125, '복사지':500}
n = int(input("파악 재고수 기준: "))
for i in items:
    if items[i] < n:
        print(i, ":", items[i])
     
# cpb08-3
engkor_dict = dict()
while True:
    eng = input("영어 단어 입력: ")
    kor = input("한글 단어 입력: ")
    if eng == "" and kor == "":
        break
    engkor_dict[eng] = kor

print(engkor_dict)






















