numbers = [4, 5, 6, 7, 8, 9, 10]

def summa(number_list):
    result = 0
    for i in number_list:
        result += i
    return result

print(summa(numbers))
