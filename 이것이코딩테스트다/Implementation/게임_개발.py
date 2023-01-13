## 맵 안에서 움직이는 시스템을 개발
## N X M -> 각각의 칸은 육지 또는 바다
## 캐릭터는 동서남북 중 한 곳을 바라본다
## 맵은 (A, B)로 나타내어 진다 A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수
## 바다는 갈 수 없다

## 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다
## 왼쪽 방향에 가보지 않은 칸이 존재한다면 왼쪽으로 회전하고 왼쪽으로 한 칸 전진
## 왼쪽 방향에 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다
## 만약 네 방향 모두 가본 칸이거나 바다로 되어 있는 칸인 경우, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로, 만약 뒤가 바다라면 움직임을 멈춤

# N X M 입력
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 현재 위치를 좌표로 입력
x, y, direction = map(int, input().split())

# 현재 위치를 1로 하여 방문 처리 
d[x][y] = 1

# 전체 맵 정보 저장
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 정의
def turn_left():
    global direction # global로 지정해주어서 외부 변수 사용
    direction -= 1
    if direction == -1: # 만약 한 바퀴 다 돌면 초기화
        direction = 3

# 시작
count = 1 # 현자리도 포함
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전하고 만약 가보지 않았다면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] == 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else: # 회전 이후 정면에 다 가봤거나 바다인 경우
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        nx = y - dy[direction]
        # 뒤로 갈 수 없다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다인 경우
        else:
            break
        turn_time = 0

print(count)