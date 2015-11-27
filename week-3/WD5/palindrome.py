
def create_palindrome(str):
        i = len(str)-1
        reversed = ""
        while i >= 0:
            reversed += str[i]
            i -= 1
        return reversed

original = "pear"
output = create_palindrome(original)
print(original + output)
