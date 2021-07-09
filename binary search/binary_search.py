def binary_search(arr, x):
    l, r, = 0, len(arr)-1
    #l이 r보다 작거나 같을 동안
    while l <= r:
        m = (r + l) // 2
        #중간값이 타겟값과 같을 경우 위치 리턴
        if arr[m] == x:
            return m
        #중간값보다 타겟값이 작을 경우 중간값의 왼쪽 영역 탐색
        elif x < arr[m]:
            r = m - 1
        #중간값보다 타겟값이 크거나 같을 경우 중간값의 오른쪽 영역 탐색
        else:
            l = m + 1
    return -1

if __name__ == '__main__' :
    arr = list(map(int, input().split()))
    x = int(input())
    print(binary_search(arr, x))
