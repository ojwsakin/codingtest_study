## N X M 크기의 직사각형 형태의 미로
## 시작 위치 (1, 1)
## 괴물이 있는 부분 0, 없는 부분 1
## 내가 움직일 때는 한 칸씩 움직일 수 있음
## 탈출하기 위해 움직여야 하는 최소 칸의 개수
## 시작 칸과 마지막 칸을 모두 포함

## 해결 방안
# BFS사용 -> why? bfs는 시작 지점에서 가까운 노드부터 차례대로 
# 그래프의 모든 노드를 탐색
# 그러므로 (1, 1)부터 시작해서 모든 노드의 값을 거리 정보로 삽입

# brs사용 위해 import
from collections import deque

# data 입력
n, m = map(int, input().split())

# 2차원으로 데이터 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의
# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs구현
def bfs(x, y):
    # queue구현을 위해 deque이용
    queue = deque()
    queue.append((x, y))
    # queue가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현 위치에서 네 방향으로의 위치
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 공간 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue
            # 벽인 경우 무시 (벽 = 0)
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))
