def binary_search(arr, x):
    l, r, = 0, len(arr)-1
    while l <= r:
        m = (r + l) // 2
        if arr[m] == x:
            return m
        elif x < arr[m]:
            r = m - 1
        else:
            l = m + 1
    return -1

if __name__ == '__main__' :
    arr = list(map(int, input().split()))
    x = int(input())
    print(binary_search(arr, x))
