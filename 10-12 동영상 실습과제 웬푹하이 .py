###6.1.1
##import turtle
##f = turtle
##f.shape('turtle')
##f.rt(90)
##f.forward(100)
##f.rt(90)
##f.forward(100)
##f.rt(90)
##f.forward(100)
##f.rt(90)
##f.forward(100)

###6.1.2
##list1 = [1,2,3,4,5]
##list2 = ['a', 'b', 'c']
##list3 = [1,'a', "abc", [1,2,3]]

##for i in [1,2,3,4,5]:
##    print("파이썬")
##
###for i in range(start, stop, step)
##for i in range(1,6,1):
##    print("파이썬")


#program p06-01
##s = 0 
##for i in [1,2,3,4,5]:
##    s += i
##    print("s :", s)
##

##s = 0 
##for i in [1,2,3,4,5]:
##    s += i
##    print("i: ", i, ", s : ", s )
##    print("s :", s)

# comment !!! coding 1
##s = 0
##for i in [5,4,3,2,1]:
##    s = s + i
##print("s : ", s)
##
##s = 0
##for i in range(5, 0, 1):
##    s = s + i
##print("s : ", s)

# program p06-02
##
##for i in range(1,6,1):
##    print(i, end="")
##

#thinking !!! 2
##for i in range(1,6,1):
##    print(i, end="")
##    
##print("")
##    
##for i in range(0,5,1):
##    print(i, end="")

#comment !!! coding 2

##s = 0
##for i in range (1,10,1):
##    s += i
##    print("i : ", i,"s: ", s)
##print(" ")
##
###comment !!! coding 3
##s = 0
##for i in range (10,0,-1):
##    if i % 2 == 1:
##        s += i
##        print("i : ", i,"s: ", s)

# 6.2 while
##i = 1
##s = 0
##while i <= 5:
##    s += i
##    print(i, s)
##    i = i + 1

#program p06-03
##
##n = 1
##s = 0
##while n <= 10:
##    if n % 2 == 0:
##        s += n
##        print("n: ", n, "s: ", s)
##    n +=1
##print("s: ", s)
##
##print(" ")
##
##n = 10
##s = 0
##while n > 0:
##    if n % 2 == 0:
##        s += n
##        print("n: ", n, "s: ", s)
##    n -=1
##print("s: ", s)

#comment !!! coding 4
##n = 2
##s = 0
##while n <= 10:
##    s += n
##    print("n: ", n, "s: ", s)
##    n +=2
##print("s: ", s)
##print(" ")

#comment !!! coding 5
##n = 9
##s = 0
##while n > 0:
##    s += n
##    print("n: ", n, "s: ", s)
##    n -=2
##print("s: ", s)


# 6.3
##for i in [1,2,3,4,5]:
##    if i == 5:
##        break
##
##    if i % 2 == 0:
##        continue
##    print(i, end=" ")
##print(" ")
##print(i)


# 6.4
s = 0
for i in range(1,21,1):
    if i % 2 == 1:
        continue
    s += i
    print("i: ", i, "s: ", s)
    if s > 30:
        break
print(" ")
print("i: ", i, "s: ", s)















    
