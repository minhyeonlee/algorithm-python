'''
1467 : [기초-배열연습] 2차원 배열 순서대로 채우기 1-8
다음과 같은 n*m 배열 구조를 출력해보자.

입력이 3 4인 경우 다음과 같이 출력한다.
10 7 4 1
11 8 5 2
12 9 6 3

입력이 4 5인 경우는 다음과 같이 출력한다.
17 13 9 5 1
18 14 10 6 2
19 15 11 7 3
20 16 12 8 4

입력이 n m인 경우의 2차원 배열을 출력해보자.
'''
n, m = input().split()
n = int(n)
m = int(m)
for i in range(n-1, -1, -1):
    for j in range(m):
        print(n*m-i-(j*n), end=" ")
    print()