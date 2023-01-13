# Python스러운 code
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 만약 리스트에 하나만 남았다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # pivot은 첫 원소
    tail = array[1:] # 두번째 원소부터 생각해야 할 원소들

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x >= pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


