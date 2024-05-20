def merge(arr, s, mid,  e):
    # mid = s + (e - s) // 2
    arr1 = arr[:mid]
    arr2 = arr[mid:]

    print(arr1, arr2, arr)
    i , j = 0, 0
    # merged_arr = []
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):
        arr[k] = arr1[i]
        k += 1
        i += 1
    while j < len(arr2):
        arr[k] = arr2[j]
        k += 1
        j += 1
    print(arr)

def mergeSort(arr, n):
    # Write your code here.
    if n <= 1:
        return;
    mid = n // 2
    # print(mid)
    mergeSort(arr[0:mid], len(arr[0:mid]))
    mergeSort(arr[mid:], len(arr[mid:]))
    merge(arr, 0, mid, n-1)
    

if __name__ == '__main__':
    arr = [4,3,1,2]
    mergeSort(arr, len(arr))
    print(arr)