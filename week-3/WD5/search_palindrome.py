def is_palindrome(word):
    return word == word[::-1] and len(word) >= 3

def search_palindromes(list):
    splitstring_list = list.split(" ")
    result = []

    for word in splitstring_list:
        for i in range(0, len(word)-1):
            for j in range(i+1, len(word)):
                variable = word[i:j+1]
                if is_palindrome(variable):
                    result.append(variable)
    return result

output = search_palindromes('dog goat dad duck doodle never')
print(output)
