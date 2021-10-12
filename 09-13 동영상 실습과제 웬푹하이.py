#09-13 실습내용

##x=1
##x=2
##print(x) #결과값: 2출력
##
### 연산 응용이 가능함
##x=1
##y=2
##print(x,y)
##
##x=x+3
##y=y+3
##z=x+y
##print(x,y,z)
'''
#저장된 문잔ㅇ를 주석처리하고 십다. (두가지 방법)
#1방법 ''' '''
#2방법 주석 설정 범위 설정 드래그+ alt 3
      주석 해제 범이 설정 그래그 +alt 4

'''

##x=3
##y=4
##print(x,y)
##
##x=3
##y=x
##print(x,y)
##
##x=3
##y=4
##z=x
##x=y
##y=z
##print(x,y,z)

#잠깐 코딩
#3
####varname=1
####VarName=3
####print(varname, VarName) #1, 3
####
#####4
####a=3
####b=5
####c=a*a+b*b
####print(a,b,c)
####
#####5
####s1= "파미썬"
####s2= " "
####s3= "프로그래밍"
####print(s1,s2,s3, "은 참 재미이다")

#다중대입문

#동일한값
##a=b=c=1
##print(a,b,c)
#서로 다른 값을 입력
#a,b,c= 1,2,3 #양쭉의 갯수가 일치해야
##a,b,c= 1,2, 3.14
##
##print(a,b,c)

#3.2.1 사용자로부터

##name= input("첫번째 이름은 입력해주세요: ")
### 모니터 대기모드에 데이터 입력
##print(name, "입력되었습니다.")
##
##hakbun= input("두바째 학번 입력해 주세요: ")
##print(hakbun, "번입니다.")
##
##univ_name = input("대학교명: ")
##
##univ_dept = input("학과명: ")
##
##print("대학교명: ", univ_name,"학과명: ",univ_dept, "이름: ",name,"학번:", hakbun)

# input 명령어는 입력된 문자로만 인식 (숫자도 문자인석)
#석숫자 데이터는 연산 이용 불가 오류 ㅁ니ㅣ세지
#지밧드시 형 변환이 필요합니다.
##
##x=input("정수1 입력: ")
##y=input("정수2 입력: ")
##z=x+y
##print(x,y,z)
##
##x=int(input("정수1 입력: "))
##y=int(input("정수2 입력: "))
##z=x+y
##print(x,y,z)
#데이터자료형 확인하기
#기프로그랭 03-04

x=1
y=3.14
z= "text string"

print(x, type(x))
print(y, type(x))
print(z, type(x))

#잠깐 코딩
fnum= input("실수 입력: ")
print(fnum, type(fnum))

fnum= float(input("실수 입력: "))
print(fnum, type(fnum))

















