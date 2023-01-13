## 정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 4가지

## X가 5로 나누어떨어지면, 5로 나눈다
## X가 3으로 나누어떨어지면, 3으로 나눈다
## X가 2로 나누어떨어지면, 2로 나눈다
## X에서 1을 뺀다

## 정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만든다
## 연산을 사용하는 횟수의 최솟값 출력

## Bottom-up 방식으로 접근
## 기준은 -1을 하는 것이 좋다 
## 나머지는 명확하게 나눠지니깐

# X 입력 받기
x = int(input())

## Bottom-up하는 결과를 저장 할 리스트 생성
list = [0] * 30001

for num in range(2, x + 1):

    # 현재에서 1을 빼는 경우의 수 - 기준
    list[num] = list[num - 1] + 1

    if num % 5 == 0:
        list[num] = min(list[num], list[num // 5] + 1)
    
    if num % 3 == 0:
        list[num] = min(list[num], list[num // 3] + 1)
    if num % 2 == 0:
        list[num] = min(list[num], list[num // 2] + 1)
    
print(list[x])