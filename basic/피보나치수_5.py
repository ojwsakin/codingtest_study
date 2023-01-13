## 피보나치 수는 0과 1로 시작.
## 0, 1, .....
## 앞 두 수의 합
## n이 주어졌을 때, n번째 피보나치를 수를 구하는 프로그램을 작성

## 입력 : n은 20보다 작거나 같은 자연수 또는 0

# 입력 저장
n = int(input())

# 피보나치 수는 3개 이상부터 함수를 실행 -> 재귀 함수로 구현
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(n))