'''
Select an element and place it on correct index in sorted part
'''
def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        curr_ind = i
        for j in range(i,-1,-1):
            if arr[j] > arr[curr_ind]:
                arr[j], arr[curr_ind] = arr[curr_ind], arr[j]
                curr_ind = j
    return arr
arr = [9,8,5,3,4,1]
print(insertion_sort(arr))