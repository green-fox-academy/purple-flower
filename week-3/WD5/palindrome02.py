def create_palindrome(str):
    return str + (str[::-1])

output = create_palindrome("pear")
print(output)
