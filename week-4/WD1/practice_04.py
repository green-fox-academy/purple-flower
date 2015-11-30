# create a function that returns its input factorial

def factor(input):
    output = 1
    i = 1
    while i <= input:
        output *= i
        i += 1
    return output

print(factor(6))

#2

def factor2(input):
    output = 1
    for n in range(1, input + 1):
        output *= n
    return output

print(factor2(7))

# recursive solution

def factor3(input):
    if input == 1:
        return 1
    else:
        return factor3(input-1) * input

print(factor3(3))
