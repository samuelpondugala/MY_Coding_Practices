def is_palindrome1(s):
    res = s == s[::-1]
    return res
def is_palindrome2(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
a = is_palindrome2("racecar")
print(a)
