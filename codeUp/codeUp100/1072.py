'''
1072 : [기초-반복실행구조] 정수 입력받아 계속 출력하기(설명)
n개의 정수가 순서대로 입력된다.
-2147483648 ~ +2147483647, 단 n의 최대 개수는 알 수 없다.

n개의 입력된 정수를 순서대로 출력해보자.

while( ), for( ), do~while( ) 등의 반복문을 사용할 수 없다.
'''
#입력할 정수의 개수 n
n = int(input())
#n개의 정수를 공백을 두고 입력
list = input().split()

for x in list:
    print(int(x))