## 1번역(출발역) 10번역(종착역) 까지 10개의 정차역이 있는 노선
## 이 기차에는 타거나 내리는 사람 수를 자동으로 인식할 수 있는 장치가 존재
## 이 장치를 이용하여 출발역에서 종착역까지 가는 도중 기차 안에 사람이
## 가장 많을 때의 사람 수를 계산
## 단, 질서를 잘 지킨다. 또한 내릴 사람이 모두 내린 후에 기차에 탄다

## 추가 조건 ##
## 기차는 역 번호 순서대로 운행
## 출발역에서 내린 사람 수와 종착역에서 탄 사람 수는 0
## 각 역에서 현재 기차에 있는 사람보다 더 많은 사람이 내리는 경우는 없다
## 기차의 정원 = 10,000

# 각 역 사람 수 list 생성
num = []
person = 0

# 1번째 데이터 입력 받고 초기 설정
n_1, k_1 = map(int, input().split())
num.append(k_1 - n_1)
person = num[0]

# 입력값 받기
for i in range(1, 10):
    n, k = map(int, input().split())
    person += (k - n)
    num.append(person)

# list 에서 최댓값 출력
max = 0
for i in num:
    if i > max:
        max = i

print(max)