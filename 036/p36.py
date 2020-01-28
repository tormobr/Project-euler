
def solve():
    res = 0
    for n in range(1000000):
        if is_palindrome(str(n)) and is_palindrome(bin(n)[2:]):
            res += n
    return res

def is_palindrome(n):
    return n == n[::-1]

print(solve())
