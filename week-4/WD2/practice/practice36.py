numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list

def reverse(input_list):
    reverse_list = []
    i = len(input_list)-1
    while i >= 0:
        reverse_list.append(input_list[i])
        i -= 1
    return reverse_list

numbers = reverse(numbers)
print(numbers)
