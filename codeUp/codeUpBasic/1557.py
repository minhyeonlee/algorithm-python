'''
1557 : [기초-함수작성] 함수로 n의 약수의 개수 리턴하기
int 형 자연수 한 개를 입력 받아
약수의 개수를 출력하시오.
예를 들어,
자연수 8은 1, 2, 4, 8 로 나누어떨어지므로 약수가 4개 이다.
단, 함수형 문제이므로 함수 f()만 작성하여 제출하시오.
'''
def f(n):
    cnt = 0
    for i in range(1, n+1):
        if(n%i==0):
            cnt = cnt+1
    return cnt

n = int(input())
print(f(n))