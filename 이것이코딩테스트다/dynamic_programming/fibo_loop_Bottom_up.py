## Bottom-up
## 반복문 사용

list = [0] * 100

## 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
list[1] = 1
list[2] = 1
n = 99

## 피보나치 함수를 반복문으로 구현
for i in range(3, n+1):
    list[i] = list[i-1] + list[i-2]

print(list[n])