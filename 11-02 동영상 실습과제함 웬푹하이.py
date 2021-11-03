### 8.1 program coding

##comp_dict = {'A' : 'T' , 'T' : 'A' , 'C' : 'G' ,'G' : 'C'}
##print(comp_dict)
##print(len(comp_dict))
##print(comp_dict.keys())
##print(comp_dict.values())
##
##print(comp_dict["T"])
##
##### 8.2 program coding
##
##def comp(seq):
##    seq_comp = ""
##    for char in seq:
##        seq_comp = seq_comp + comp_dict[char]
##    return seq_comp
##def rev(seq):
##    seq_rev = "".join(reversed(seq))
##    return seq_rev
##def rev_comp(seq):
##    temp = comp(seq)
##    return rev(temp)
##
###메인 선언
##src = input("DNA sequence: ")
##cnvt = int(input("1(comp), 2(rev), 3(rev_comp)"))
##if (cnvt >= 1 and cnvt <=3):
##    if (cnvt == 1):
##        rst = comp(src)
##
##    elif (cnvt == 2):
##        rst = rev(src)
##    else:
##        rst = rev_comp(src)
##    print(src, "->", rst)
##else :
##    print("재입력 요청" , "1(comp), 2(rev), 3(rev_comp)")


### thinking1
##
###comp_dict = {'A' : 'T' , 'T' : 'A' , 'C' : 'G' ,'G' : 'C'}
##def comp(seq):
##    seq_comp = ""
##    for char in seq:
##        if char in comp_dict:
##            seq_comp = seq_comp + comp_dict[char]
##        else :
##             seq_comp = seq_comp + '?'
##    return seq_comp
##def rev(seq):
##    seq_rev = "".join(reversed(seq))
##    return seq_rev
##def rev_comp(seq):
##    temp = comp(seq)
##    return rev(temp)
##
###메인 선언
##comp_dict = {'A' : 'T' , 'T' : 'A' , 'C' : 'G' ,'G' : 'C'}
##src = input("DNA sequence: ")
##cnvt = int(input("1(comp), 2(rev), 3(rev_comp)"))
##if (cnvt >= 1 and cnvt <=3):
##    if (cnvt == 1):
##        rst = comp(src)
##
##    elif (cnvt == 2):
##        rst = rev(src)
##    else:
##        rst = rev_comp(src)
##    print(src, "->", rst)
##else :
##    print("재입력 요청" , "1(comp), 2(rev), 3(rev_comp)")


### thinking2

#comp_dict = {'A' : 'T' , 'T' : 'A' , 'C' : 'G' ,'G' : 'C'}
##def comp(seq):
##    seq_comp = ""
##    for char in seq:
##        if char in comp_dict:
##            seq_comp = seq_comp + comp_dict[char]
##        else :
##             seq_comp = seq_comp + '?'
##    return seq_comp
##
##def rev(seq):
##    seq_rev = "" #.join(reversed(seq))
##    n = int(len(seq)) - 1
##    while n > 1:
##        seq_rev = seq_rev + seq[n]
##        n = n - 1
##    return seq_rev
##
##def rev_comp(seq):
##    temp = comp(seq)
##    return rev(temp)
##
###메인 선언
##comp_dict = {'A' : 'T' , 'T' : 'A' , 'C' : 'G' ,'G' : 'C'}
##src = input("DNA sequence: ")
##cnvt = int(input("1(comp), 2(rev), 3(rev_comp)"))
##if (cnvt >= 1 and cnvt <=3):
##    if (cnvt == 1):
##        rst = comp(src)
##
##    elif (cnvt == 2):
##        rst = rev(src)
##    else:
##        rst = rev_comp(src)
##    print(src, "->", rst)
##else :
##    print("재입력 요청" , "1(comp), 2(rev), 3(rev_comp)")


### Comment coding 1

digit = { 1: '일', 2:'이', 3:'살'}
print(digit)
print(len(digit))
print(digit.keys())
print(digit.values())
print(digit[1])
print(digit[3])

### Comment coding 2

fruit =  {'사과':100, '바나나':50, '수박': 1000}
print(fruit)
print(len(fruit))
print(fruit.keys())
print(fruit.values())
print(fruit['사과'])
print(fruit['수박'])










