numbers = [3, 4, 5, 6, 7]
#write a function that filters the odd numbers from a list and
#returns a new list consisting only the evens
even_list = []

def odd_numbers(input_list):
    i = 0
    while i <= (len(input_list)-1):
        if input_list[i] % 2 == 0:
            even_list.append(input_list[i])
        i += 1
    return even_list

numbers = odd_numbers(numbers)
print(even_list)
