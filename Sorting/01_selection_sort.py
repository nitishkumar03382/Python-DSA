defn = '''select the minimum element in a range 
and swap that with first element of the range'''
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] # Swap the first index of range to min element
    return arr
arr = [4,5,2,1,7,9]
print(selection_sort(arr))


