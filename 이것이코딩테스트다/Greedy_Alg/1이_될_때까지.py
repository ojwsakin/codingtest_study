## 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
## 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택
##      1. N에서 1을 뺀다
##      2. N을 K로 나눈다

## ex) N = 17, K = 4 이라고 가정
##     1번 과정 1번 -> 16
##     2번 과정 1번 -> 4
##     2번 과정 1번 -> 1
##     따라서 연산 횟수는 "3"

# 입력
n, k = map(int, input().split())

# count 변수 설정
count = 0

## k로 나눠지는지 판단
while True:
    if n % k == 0:
        n = n // k
    else:
        n -= k
    count += 1
    if n == 1:
        break

# 결과 출력
print(count)
    
