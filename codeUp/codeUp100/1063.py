'''
1063 : [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기(설명)
입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.
'''
x,y = input().split()
x = int(x)
y = int(y)
print(x if x>y else y)