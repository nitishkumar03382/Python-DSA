def largest( arr, n):
    maxi = -1
    for x in arr:
        maxi = max(x, maxi)
    return maxi