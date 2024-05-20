def linear_search(arr, size, target):
    if size == 0:
        return False
    if arr[0] == target:
        return True
    else:
        ans = linear_search(arr[1:], size - 1, target)
        return ans

if __name__ == '__main__':
    arr = [33, 1, 2, 55, 5, 8]
    target = 56
    ans = linear_search(arr, len(arr), target)

    print(ans)