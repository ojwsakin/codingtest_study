## N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오

## 첫째 줄 - 정수의 개수 N
## 둘째 줄 - N개의 정수를 공백으로 구분해서 주어진다.
## -1,000,000, 1,000,000 사이의 수

## 출력 : 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력

# N 입력
n = int(input())

# list input
n_list = map(int,input().split())

# 최소, 최대 초기화
# min(), max() 사용 안하고 구현

# 최솟값과 최댓값 구하기
min = 1000001
max = -1000001

for i in n_list:
    if i < min:
        min = i
    if i > max:
        max = i

print(min,max)