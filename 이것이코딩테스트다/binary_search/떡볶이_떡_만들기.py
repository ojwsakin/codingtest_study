## 떡의 길이가 일정 하지 않다
## 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다
## 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단
## H보다 긴 떡은 잘리고, H보다 작은 떡은 안잘린다
## 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값
## 4 6
## 19 15 10 17
## 출력 : 15

# 입력 받기 
n, request = map(int, input().split())

# 떡의 길이 입력 받기
data = list(map(int, input().split()))

# 이진 탐색을 사용!
# Parametric Search문제

#### 내가 푼 답안은 아래에 있음....진짜 이상하게 풀어서 밑으로 내림...
#####

# 떡의 길이 중 가장 긴 길이를 변수로 받아옴
end = max(data)
start = 0
result = 0

# 0부터 max_l까지 이제 이진 탐색을 하면 된다! -> 내가 여기서 너무 이상하게 생각함

while (start <= end):
    total = 0
    # mid 설정
    mid = (start + end) // 2
    
    for i in data:
        if i > mid:
            total += (i - mid)
    
    ## total 값이 request보다 크면 떡을 더 잘라야 한다
    if total > request:
        start = mid + 1
    elif total < request:
        end = mid - 1
    else:
        result = mid
        break

print(result)










# ###### 왜 연속된 자연수를 리스트로 넣는 바보같은 짓을 한거지..?
# # 떡볶이 떡의 최대 길이를 찾아서 0부터 최대 길이를 설정하고, 찾아 가며 계산
# max_l = max(data)
# # 이진 탐색을 위한 데이터 생성
# list = [x for x in range(max_l + 1)] # 0으로도 자를 수 있고, 높이의 최대로도 자를 수 있다
# start = 0
# end = max_l
# # 정답을 담을 변수 설정
# solution = 0
# # 반복문 실행
# while True:
#     answer = 0
#     mid = (start + end) // 2

#     for i in data:
#         if i >= list[mid]:
#             answer += (i-list[mid])
    
#     if request == answer:
#         solution = mid
#         break
#     elif request < answer:
#         start = mid + 1
#     else:
#         end = mid - 1

# print(solution)
