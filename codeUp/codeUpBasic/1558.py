'''
1558 : [기초-함수작성] 함수로 정수 뒤집어 리턴하기
long long int 형 정수 한 개를 입력 받아
숫자를 거꾸로 뒤집은 수를 출력하시오.
(단, 마지막 1의 자리의 수가 0인 수는 입력되지 않는다.)
예를 들어
123456789 를 거꾸로 뒤집은 수는 987654321 이다.
단, 함수형 문제이므로 함수 f()만 작성하여 제출하시오.
'''
def f(n):
    lst = ""
    for i in range(len(n)-1, -1, -1):
        lst = (lst + n[i])
    return lst

n = input()
print(f(n))