'''
Take the max element to end by comparing the adjacent elements
'''
def bubble_sort(arr):
    n = len(arr)
    for i in range (n-1, -1, -1):
        print(i, end = '=>')
        for j in range(0, i):
            print(j, end = ' ')
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
arr = [9,8,5,3,4,1]
print(bubble_sort(arr))
