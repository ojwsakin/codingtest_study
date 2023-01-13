## 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다
## 뽑고자 하는 카드가 포함되어 있는 행을 선택
## 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다
## 카드 뽑을 경우 수 중 가장 높은 카드를 뽑을 경우가 이기는 게임

# 첫 째줄 입력 -> 데이터 형태
n, m = map(int, input().split())

####### 내가 푼 정답 ########
# 정답 리스트 생성
answer = []

# 반복문을 활용하여 데이터 입력
for i in range(n):
    cal = list(map(int, input().split()))
    cal.sort()
    answer.append(cal[0])  # 행에서 가장 작은 수 선택

# 정답 리스트 정렬 후 가장 큰 수 추출
answer.sort()
print(answer[-1])
