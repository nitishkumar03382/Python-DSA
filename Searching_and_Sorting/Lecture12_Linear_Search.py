def linear_search(arr, size, target):
    for i in range(size):
        if arr[i] == target:
            return i
    return -1

if __name__ == '__main__':
    arr = [1,5,2,3,4,11]
    target = 4
    index = linear_search(arr, len(arr), target)
    print(index)