''''
기초4-1. 단순 반복문
1075 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2(설명)
정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
'''
i = 0
x = int(input())
for i in range(x):
    i+=1
    print(x-i)