# 반복문을 통한 이진 탐색 소스코드 구현

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target < array[mid]:
            end = mid - 1
        elif target > array[mid]:
            start = mid + 1
        else:
            return mid
    return None

n, target = map(int, input().split())

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
    print("원소가 없음")
else:
    print(array[result]) 