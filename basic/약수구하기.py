## 어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수
## 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램
## 입력은 첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다.
## 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우 0을 출력

# N의 약수 리스트 생성
list_n = []

# 입력된 데이터 저장
n, k = map(int,input().split())

# N의 약수 계산
for i in range(1, n + 1):
    if n % i == 0:
        list_n.append(i)

# N의 약수의 개수와 K를 비교하고 작으면 0을출력
# 위 조건이 아닐 경우 정답 출력
if len(list_n) < k:
    print(0)
else:
    print(list_n[k - 1])