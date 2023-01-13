## N X M 크기의 얼음 틀이 존재
## 구명이 뚫려 있는 부분 0, 칸막이가 존재하는 부분 1
## 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주

## 해결 방안
# graph라 생각하고 접근해보자 -> why? 2차원 배열이니까
# 처음 받을 데이터들을 받고 
# 탐색을 시작하는데, DFS로 접근한다
# 모든 노드에서 탐색을 할 꺼고, 방문한 노드는 1로처리해
# 다음 반복에서 중복으로 같은 경로가 나오지 않게 한다

# 데이터 입력
n, m = map(int,input().split())

# 2차원 배열로 리스트 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# dfs 정의
def dfs(x, y):
    # 만약 값이 벗어났다면 return False
    # 잘 생각해야 하는 사항이 왜 x가 n보다 크거나 같을 때 인가
    # 상하좌우 살필 때 x + 1을 하므로!!
    if x >= n or x <= -1 or y <= -1 or y >= m:
        return False
    # 만약 주어진 곳이 비어 있다면
    if graph[x][y] == 0:
        # 상, 하, 좌, 우를 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    # else 일 경우
    return False 

# 결과값을 저장 할 변수 설정
result = 0

# 모든 노드에 대해 계산
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)