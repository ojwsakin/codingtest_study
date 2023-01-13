## 일과를 마치고 온 난쟁이가 7명이 아닌 9명이다.
## 일곱 난쟁이 키의 합이 100이다
## 아홉 난쟁이의 키가 주어졌을 때, 일곱 난쟁이를 찾는 프로그램 작성

## 키는 100을 넘지 않는 자연수
## 아홉 난쟁이의 키는 모두 다르다
## 가능한 정답이 여러가지인 경우에는 아무거나 출력
## 일곱 난쟁이의 키를 오름차순으로 출력. 일곱 난쟁이를 찾을 수 없는 경우는 없다

# 데이터 입력
n_list = []

for i in range(9):
    n_list.append(int(input()))

# 데이터 정렬
n_list.sort()

# 아홉 난쟁이 키의 합
sum = 0
for i in n_list:
    sum += i

# 조합의 경우로 해결..? 9C7 = 36가지의 경우의 수

# target index 선언 & 초기화
index_i = 0
index_j = 0

# 이중 for문 작성
for i in range(8):
    for j in range(i + 1, 9):
        if n_list[i] + n_list[j] == sum - 100:
            index_i = i
            index_j = j

# 해당 index 를 n_list 에서 제거
del1 = n_list[index_i]
del2 = n_list[index_j]

n_list.remove(del1)
n_list.remove(del2)

# 출력
for i in n_list:
    print(i)
            
   


        