## 정원 = 8 X 8
## 나이트는 2가지 경우로만 움직일 수 있다.
## 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
## 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동

## 행 위치는 1부터 8
## 열 위치는 a부터 h

## 나이트의 위치가 주어질 때 움직일 수 있는 경우의 수 계산

######## 나의 풀이 #########
input = input()

# 행 데이터 
row = int(input[1])

# 열 데이터
column = int(ord(input[0])) - int(ord('a')) + 1

# step 생성
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

# 8가지 방향에 대햐여 경우의 수 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치가 가능한 위치인지 확인
    if next_row >=1 and next_column <= 8 and next_row <= 8 and next_column >= 1:
        result += 1

print(result)
