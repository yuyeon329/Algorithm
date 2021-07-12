def counting_sort(arr):
    n = max(arr)+1
    cnt = [0]*n
    sorted = []

    #중복된 값의 개수를 해당 idx에 저장
    for i in arr:
        cnt[i] += 1

    #중복된 만큼 차례대로 idx 출력
    for i in range(n):
        for j in range(cnt[i]):
            sorted.append(i)

    return sorted

if __name__ == '__main__' :
    arr = list(map(int, input().split()))
    print(counting_sort(arr))