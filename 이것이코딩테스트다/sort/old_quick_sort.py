array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

## 재귀함수로 구현
def quick_sort(array, start, end):
    if start >= end: # 종료 조건 : 원소가 1개인 경우
        return
    pivot = start
    left = start + 1
    right = end
    
    while left <= right: # 반복문 탈출 종료 조건 
        
        # pivot보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot보다 작은 데이터를 찾을 때까지 반복
        while right >= start and array[right] >= array[pivot]:
            right -= 1
        
        if left > right: # 엇갈린 경우 이므로 pivot의 위치를 바꿔주고 큰 while문 탈출
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[right], array[left] = array[left], array[right]

    # 분할 이후 재귀 호출
    quick_sort(array, start, right - 1)
    quick_sort(array, right+ 1, end)

quick_sort(array, 0, len(array)-1)
print(array)