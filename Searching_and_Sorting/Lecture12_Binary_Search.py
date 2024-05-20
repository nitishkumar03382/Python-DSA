def binary_search(arr, start, end, target):
    while start <= end:
        mid = start + ((end - start) // 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

if __name__ == '__main__':
    #### TEST CASES ####
    # arr = [1, 4, 6, 8, 11, 25 ,32]
    # arr = [32]
    # arr = [1]
    arr = []
    # target = 11
    # target = 111
    # target = 1
    target = 32
    index = binary_search(arr, 0, len(arr) - 1, target)
    print(index)