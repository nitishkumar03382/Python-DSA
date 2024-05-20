def array_sum(arr, size):
    if size == 0:
        return 0
    return arr[0] + array_sum(arr[1:], size - 1)

if __name__ == '__main__':
    #### TEST CASES ####
    arr = [1,5,2,1,3,4]
    # arr = [1]
    # arr = []
    sum = array_sum(arr, len(arr))
    print(sum)