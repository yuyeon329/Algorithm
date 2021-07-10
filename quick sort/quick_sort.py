def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr)//2]
    smaller_arr, equal_arr, bigger_arr = [], [], []
    print("arr ", arr)
    print("pivot ", pivot)

    for i in arr:
        if i<pivot:
            smaller_arr.append(i)
        elif i>pivot:
            bigger_arr.append(i)
        else:
            equal_arr.append(i)
    return quick_sort(smaller_arr) + quick_sort(equal_arr) + quick_sort(bigger_arr)


if __name__ == '__main__' :
    arr = list(map(int, input().split()))
    print(quick_sort(arr))