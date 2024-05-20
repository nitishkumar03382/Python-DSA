def binary_search(arr, start, end, target):
    if start > end:
        return -1
    mid = start + ((end - start) // 2)
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        ans = binary_search(arr, start, mid - 1, target)
    else:
        ans = binary_search(arr, mid + 1, end, target)
    return ans

if __name__ == '__main__':
    # Test Cases
    # arr = [1,4,5,8,9,22,44]
    # arr = [1]
    arr =[]
    # target = 22
    # target = 1
    # target = 0
    target = 44
    target_index = binary_search(arr, 0, len(arr) - 1, target)
    if target_index == -1:
        print('Target not found')
    else:
        print('Target found at', target_index)