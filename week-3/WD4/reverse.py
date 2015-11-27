def reverse(in_list):
    i = len(in_list)-1
    output = []
    while i >= 0:
        output.append(in_list[i])
        i -= 1
    return output

output = reverse([1, 2, 3, 4])
print(output)
