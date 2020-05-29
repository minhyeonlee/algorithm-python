'''
3047: ABC

문제:
세 수 A, B, C가 주어진다. A는 B보다 작고, B는 C보다 작다.
세 수 A, B, C가 주어졌을 때, 입력에서 주어진 순서대로 출력하는 프로그램을 작성하시오.

입력:
첫째 줄에 세 수 A, B, C가 주어진다. 하지만, 순서는 A, B, C가 아닐 수도 있다.
세 수는 100보다 작거나 같은 자연수이다. 둘째 줄에는 A, B, C로 이루어진 세 글자가 주어지며, 이 순서대로 출력하면 된다.

출력:
주어진 세 수를 주어진 출력 순서대로 출력하면 된다.
'''
numbers = list(map(int, input().split()))
letters = input()
numbers.sort()

for l in letters:
    if l == 'A':
        print(numbers[0], end=" ")
    elif l == 'B':
        print(numbers[1], end=" ")
    else:
        print(numbers[2])
