def quick_sort(arr):
    if len(arr) < 2:
        return arr
    #피벗 설정
    pivot = arr[len(arr)//2]

    #분할된 데이터를 담을 list
    smaller_arr, equal_arr, bigger_arr = [], [], []

    #pivot과 비교해 비교 결과에 따라 list에 넣어줌
    for i in arr:
        if i<pivot:
            smaller_arr.append(i)
        elif i>pivot:
            bigger_arr.append(i)
        else:
            equal_arr.append(i)

    #재귀적으로 호출하여 분할 진행
    return quick_sort(smaller_arr) + quick_sort(equal_arr) + quick_sort(bigger_arr)


if __name__ == '__main__' :
    arr = list(map(int, input().split()))
    print(quick_sort(arr))