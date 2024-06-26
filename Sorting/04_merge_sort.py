def merge_sorted(arr, low, mid, high):
    left = low
    right = mid + 1
    tmp = []
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            tmp.append(arr[left])
            left += 1
        else:
            tmp.append(arr[right])
            right += 1
    while left <= mid:
        tmp.append(arr[left])
        left += 1
    while right <= high:
        tmp.append(arr[right])
        right += 1
    print(tmp)
    arr[low:high+1] = tmp

def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge_sorted(arr, low, mid, high)
######################################
######################################
arr = [4,3,6,5,1,2]
merge_sort(arr, 0, len(arr)-1)
