## N명의 학생 정보
## 학생의 이름과 학생의 성적
## 성적이 낮은 순서대로 학생의 이름을 출력

## 풀이
n = int(input())

##dict 선언
dic = dict()

## 입력 저장
for i in range(n):
    key, value = input().split()
    value = int(value)
    dic[key]=value

## value를 key로 sorted
## sorted 하면 리스트로 변함
answer_sorted = sorted(dic.items(), key=lambda x:x[1])

for i in answer_sorted:
    print(i[0], end=' ')


###### 튜플로 해결 #######
array = []

for i in range(n):
    input_data = input().split()

    array.append((input_data[0], input_data[1]))

array = sorted(array, key=lambda x:x[1])

for i in array:
    print(i[0], end=' ')