## 가로의 길이가 N, 세로의 길이가 2인 직사각형의 바닥
## 1x2, 2x1, 2x2 덮개를 이용해 채운다
## 바닥을 채울 수 있는 경우의 수를 구하는 프로그램 작성

## 규칙성을 찾아서 점화식을 세우자

## N입력 받음
n = int(input())

## 항상 답이 들어갈 리스트 생성하는 거 잊지말자
answer = [0] * 1001

## 초기 값 설정
answer[1] = 1
answer[2] = 3

for i in range(3, n+1):
    answer[i] = (answer[i-1] + 2 * answer[i-2]) % 796796

print(answer[n])

