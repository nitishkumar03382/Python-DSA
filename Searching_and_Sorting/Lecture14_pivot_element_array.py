def get_pivot(arr, n):
    s, e = 0, n - 1
    ans = 0
    while s <= e:
        mid = s + (e - s) // 2
        print(mid)
        if arr[mid] >= arr[0]:
            s = mid + 1
        elif arr[mid] <= arr[n - 1]:
            ans = mid
            e = mid - 1
    return ans

if __name__ == '__main__':
    # arr = [8, 10, 17, 1, 3]
    # arr = [3, 5, 2]
    # arr = [1,2,3]
    arr = [3,1]
    print(get_pivot(arr, len(arr)))