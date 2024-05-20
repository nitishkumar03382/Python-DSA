def is_possible(boards, k, mid):
    n = len(boards)
    count = 1
    i = 0
    curr_sum = 0
    while(i < n):
        if(boards[i] + curr_sum <= mid):
            curr_sum += boards[i]
            i += 1
        else:
            count += 1
            if(count > k):
                return False
            curr_sum = 0

    return True


def findLargestMinDistance(boards:list, k:int):
    # Write your code here
    # Return an integer
    s = 0
    e = sum(boards)
    ans = -1
    while(s <= e):
        mid = s + (e - s) // 2
        if(is_possible(boards, k, mid)):
            e = mid - 1
            ans = mid
        else:
            s = mid + 1
    return ans
    pass