'''
1058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기
두 개의 참(1) 또는 거짓(0)이 입력될 때,
모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.
'''
x,y = input().split()
x = int(x)
y = int(y)

if(x==0 and y ==0):
    print(1)
else:
    print(0)