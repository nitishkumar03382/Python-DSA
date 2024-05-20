def first_occ(arr, size, key):
    # first_occ
    start = 0
    end = size - 1
    fo = -1
    if arr[0] == key:
        return 0
    while start <= end:
        mid = (end + start) // 2
        # print(start, end, mid, key)
        if arr[mid] == key and  arr[mid - 1] != key:
            fo = mid
            break
        elif arr[mid] < key:
            # print('arr[mid] < key')
            start = mid + 1
        elif arr[mid] >= key:
            # print('arr[mid] >= key')
            end = mid - 1
    return fo

def last_occ(arr, size, key):
    start = 0
    end = size - 1
    lo = -1
    if arr[end] == key:
        return end
    while start <= end:
        mid = (end + start) // 2
        # print(start, end, mid, key)
        if arr[mid] == key and  arr[mid + 1] != key:
            lo = mid
            break
        elif arr[mid] <= key:
            # print('arr[mid] < key')
            start = mid + 1
        elif arr[mid] > key:
            # print('arr[mid] >= key')
            end = mid - 1
    return lo


def total_occ(arr, size, key):
    if size == 0:
        return -1,-1
    f = first_occ(arr, size, key)
    l = last_occ(arr, size, key)
    if f == -1 and l == -1:
        return 0
    return l - f + 1

if __name__ == '__main__':
    #### Test Cases ####
    # arr = [1,4,4,55,66,100]
    arr = [4,4,4,55,66,100]
    # arr = [4,4,4,4,4,4]
    # arr = [1]
    # arr = []
    key = 5
    ans = total_occ(arr, len(arr), key)
    print(ans)