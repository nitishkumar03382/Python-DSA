def get_pivot(arr):
    n = len(arr)
    s, e = 0, n - 1
    ans = 0
    while s <= e:
        mid = s + (e - s) // 2
        if arr[mid] >= arr[0]:
            s = mid + 1
        elif arr[mid] <= arr[n - 1]:
            ans = mid
            e = mid - 1
    return ans

def b_search(arr,s, e, target):
    # print('b_search', arr)
    while s <= e:
        mid = (s + e)// 2
        # print(mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    return -1


def search(nums, target):
    p = get_pivot(nums)
    # print(p)
    ans = -1
    # if len(arr
    if target >= nums[p] and target <= nums[len(nums) - 1]:
        # print('Inside 1st if')
        ans = b_search(nums,p, len(nums) - 1, target)
    elif p >= 1 and target >= nums[0] and target <= nums[p - 1]:
        # print('inside else')
        ans = b_search(nums, 0, p - 1,  target)
    return ans

if __name__ == '__main__':
    arr = [1]
    target = 10
    ans = search(arr, target)
    print(ans)
