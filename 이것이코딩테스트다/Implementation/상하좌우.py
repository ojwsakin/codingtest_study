## 여행가 A는 N X N 크기의 정사각형 공간 위에 서 있다 -> 한 칸은 1 X 1
## A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 (1, 1)
## 이동할 계획서 -> 하나의 줄에 띄어쓰기를 기준
## L, R, U, D 중 하나의 문자가 반복적으로 적혀 있다
## 만약 N X N 크기를 벗어나게 되면 무시한다
## 출력은 도착할 지점의 좌표를 출력한다

####### 내가 푼 방법 #######

# N 입력
n = int(input())

# 계획서 리스트로 입력
plan = list(input().split())

# numpy 를 사용하지 않고 우선 전체 구현
# 따라서 행과 열의 정답 데이터를 생성
# 시작점은 (0, 0)으로 생각하고 마지막에 1씩 더할 계획 
answer_col = 0
answer_row = 0

## 조건
## L -> (0, -1)
## R -> (0, +1)
## U -> (-1, 0)
## D -> (+1, 0)

# 구현 -> for 문으로 구현
for sol in plan:
    
    if sol == 'L' and (answer_row > 0):
        answer_row -= 1
    elif sol == 'R' and (answer_row < n):
        answer_row += 1
    elif sol == 'U' and (answer_col > 0):
        answer_col -= 1
    elif sol == 'D' and (answer_col < n):
        answer_col += 1

# 결과 출력
print(answer_col + 1,answer_row + 1)

####### 해설 #######

# continue 로 조건에 벗어나는 경우 pass
# 일련의 명령에 따라서 개체를 차례대로 이동시킨다 -> "시뮬레이션 유형"

# N입력
n = int(input())
x, y = 1, 1
plans = input().split()

# 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    for i in range(len(move_types)):
        nx = x + dx[i]
        ny = y + dy[i]
    
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # 이동 수행
    x,y = nx, ny