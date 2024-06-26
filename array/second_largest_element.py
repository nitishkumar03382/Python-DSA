def print2largest(self,arr, n):
    # code here
    largest = max(arr)
    sec_largest = -1
    for x in arr:
        if x < largest and x >= sec_largest:
            sec_largest = x
    return sec_largest