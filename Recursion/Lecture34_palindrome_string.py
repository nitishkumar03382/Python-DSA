def chk_palindrome(s, i, j):
    if i > j:
        return True
    print(i, j)
    if s[i] != s[j]:
        return False
    return chk_palindrome(s, i + 1, j - 1)

print(chk_palindrome("aaababaa", 0 , 6))