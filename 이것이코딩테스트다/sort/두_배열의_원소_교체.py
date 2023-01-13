## 두 개의 배열 A와 B -> N개의 원소로 구성, 모두 자연수
## 최대 K번의 바꿔치기 연산을 수행
## A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 바꾸는 것
## 최종 목표는 A의 모든 원소의 합이 최대가 되도록 하는 것

# 입력
n, k = map(int, input().split())

# A, B입력
A = list(map(int, input().split()))
B = list(map(int, input().split()))

## A는 오름차순으로 정렬
A.sort()
## B는 내림차순으로 정렬
B.sort(reverse=True)

## 제일 작은 것 부터 비교하는데 A보다 작으면 그냥 안바꾸고 break
## 사실상 순서 대로 보면서 A가 더 크면 중지

for i in range(k):
    if A[i] > B[i]:
        break
    else:
        A[i] = B[i]


## 정답 출력
answer = 0
for num in range(len(A)):
    answer += A[num]

print(answer)