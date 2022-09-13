def is_palindrome(string):
    return string == ''.join(reversed(string))

print(is_palindrome('mama'))