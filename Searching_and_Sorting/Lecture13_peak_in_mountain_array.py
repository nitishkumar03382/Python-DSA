def findPeak(arr):
    start = 0
    end = len(arr) - 1
    while 1:
        mid = (start + end) // 2
        if (mid != 0 or mid != len(arr) - 1) and (arr[mid-1] < arr[mid] and arr[mid + 1] < arr[mid]):
            return mid
        elif arr[mid] < arr[mid+1]:
            start = mid + 1
        elif arr[mid] < arr[mid - 1]:
            end = mid - 1


if __name__ == '__main__':
    #### TEST CASES ####
    # arr = [1,2,3,8,12,6,4,3]
    # arr = [1,3,2]
    arr = [1,1,1,2,3,3,7,4]
    ans = findPeak(arr)
    print(ans)