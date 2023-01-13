## 하나의 수열에는 다양한 수가 존재
## 크기에 상관없이 나열
## 큰 수부터 작은 수의 순서로 정렬 -> 내림차순 정렬

## 첫째 줄 : 수의 개수 N
## 둘째 줄 - N + 1 줄 : 수 입력

# 풀이 

# 수열의 개수 입력
n = int(input())

# 수열을 입력 받아옴
n_list = []

for i in range(n):
    n_list.append(int(input()))

n_list.sort(reverse=True)
# n_list = sorted(n_list, reverse=True)

for num in n_list:
    print(num, end=' ')