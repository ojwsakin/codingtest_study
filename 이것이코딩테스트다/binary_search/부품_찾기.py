## 부품이 N개 존재
## 각 부품은 정수 형태의 고유한 번호가 있다
## 어느날 손님이 M개 종류의 부품을 대량으로 구매하겠다고 견적서 요청
## 부품 M개 종류를 모두 확인해서 견젹서를 작성
## 가게 안에 부품이 모두 있는지 확인하는 프로그램 작성

## 입력 조건 1 <= N <= 1,000,000 -> 1,000개 이상! 이진 탐색인지 의심
## 출력 있으면 yes, 없으면 no를 공백을 기준으로 해서 출력

## 해당 문제는 계수 정렬과, set 함수를 사용해도 풀린다는 것을 알고 있자

# ### 풀이 -> 이진 탐색 사용
import time
# 가게에 있는 총 부품의 종류 수
item_num = int(input())
# 가게에 있는 부품의 종류
item = list(map(int,input().split()))
item.sort()
# 손님이 요청한 부품의 종류 수
request_num = int(input())
# 손님이 요청한 부품의 종류
request_item = list(map(int, input().split()))
request_item.sort()

## 정렬된 데이터 -> 이진 탐색
start_time = time.time()
def binary_search(list, target, start, end):
    if start > end:
        return print("no", end=' ')
    
    mid = (start + end) // 2

    if target == list[mid]:
        return print("yes", end=' ')
    elif target < list[mid]:
        binary_search(list, target, start, mid - 1)
    elif target > list[mid]:
        binary_search(list, target, mid + 1, end)

for target in request_item:
    binary_search(item, target, 0, item_num - 1)
end_time = time.time()

print(end_time - start_time)

######################################################
# 반복문으로 이진 탐색 구현
# def binary_search_loop(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2

#         if target < array[mid]:
#             end = mid -1
#         elif target > array[mid]:
#             start = mid + 1
#         else:
#             return mid
#     return None
#######################################################

#######################################################
# ## 계수 정렬로 구현

# # N개의 부품 을 입력 받기
# n = int(input())
# array = [0] * 1000000

# # 가게에 있는 전체 부품 번호를 입력받아서 1로 기록
# for i in input().split():
#     array[int(i)] = 1

# # 손님의 정보 입력 받기 
# m = int(input())
# m_list = list(map(int,input().split()))

# start_time=time.time()
# # 비교
# for i in m_list:
#     if array[i] == 1:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')
# end_time=time.time()
# print(end_time - start_time)
#######################################################

#######################################################
## set 힘수

# n = int(input())

# ## set 함수를 사용하게 되면 단순히 특정 데이터가 존재 하는지 검사 할 때 매우 효과적으로 사용
# array = set(map(int, input().split()))

# m = int(input())

# x = list(map(int, input().split()))

# for i in x:
#     if i in array:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')
#######################################################