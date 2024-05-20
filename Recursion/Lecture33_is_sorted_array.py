def is_sorted(arr, size):
    if size == 0:
        return True
    if size == 1:
        return True
    if arr[0] > arr[1]:
        return False
    else:
        ans = is_sorted(arr[1:], size - 1)
        return ans
    

if __name__ == '__main__':
    #### TEST CASES ####
    # arr = [1,2,3,4,4,5]
    # arr = [1,2,3,44,4,5]
    # arr = []
    # arr = [1]
    # arr = [1,2]
    arr = [2,1]
    if is_sorted(arr, len(arr)):
        print('Sorted')
    else:
        print('Not Sorted')
