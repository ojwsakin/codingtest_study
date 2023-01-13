## 식량창고는 일직선으로 이어져 있다
## 각 식량창고에는 정해진 수의 식량을 저장하고 있다
## 식량창고를 선택적으로 약탈한다
## 정찰병은 일직선상에 존재하는 식량창고 중에서 서로 인접한
## 식량창고가 공격받으면 알 수 있다
## 개미들은 최소한 한 칸 이상 떨어진 식량창고를 약탈

# 점화식을 생각하자 

# 입력
n = int(input())

# 식량창고 정보 받기 
list = list(map(int, input().split()))

# 비어 있는 리스트 생성
answer = [0] * 100

## 점화식 : d[i] = max(d[i-1], d[i-2]+list[i])
answer[0] = list[0]
answer[1] = max(answer[0], list[1])
for i in range(2, n):
    answer[i] = max(answer[i-1], answer[i-2]+list[i])

# n-1 까지
print(answer[n-1])