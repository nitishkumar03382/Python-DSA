from collections import deque
def reverse(s):
    ans = ""
    st = deque()
    for ch in s:
        st.append(ch)
    while st:
        ans += st.pop()
    return ans

if __name__ == '__main__':
    s = input("Enter String: ")
    s = reverse(s)
    print("Reversed string:", s)