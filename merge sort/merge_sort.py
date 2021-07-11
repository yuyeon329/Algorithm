def merge_sort(arr):
    if len(arr) < 2:
        return arr
    #더 이상 분할 할 수 없을 때까지 데이터를 둘로 분할 해줌
    m = len(arr)//2
    l_arr = merge_sort(arr[:m])
    r_arr = merge_sort(arr[m:])
    merged_arr = []
    l, r = 0, 0

    #합치고자 하는 두 리스트의 값 중 가장 작은 값을 먼저 나열한다.
    while l < len(l_arr) and r < len(r_arr):
        if l_arr[l] < r_arr[r]:
            merged_arr.append(l_arr[l])
            l += 1
        else:
            merged_arr.append(r_arr[r])
            r += 1

    #위의 while문에서 둘 중 먼저 정렬이 끝난 리스트가 있으면 나머지 요소들과 함께 병합한다.
    merged_arr += l_arr[l:]
    merged_arr += r_arr[r:]
    return merged_arr

if __name__ == '__main__' :
    arr = list(map(int, input().split()))
    print(merge_sort(arr))