def is_fizzish(number, base):
    return number % base == 0 or str(base) in str(number)

def fizz:buzz(minimum, maximum = 100):
    fizz_number = 3
    buzz_number = 5
    n = minimum
    while n <= maximum:
        if is_fizzish(n, fizz_number) and is_fizzish(n, buzz_number):
            print('fizzbuzz')
        elif is_fizzish(n, buzz_number):
            print('buzz')
        elif is_fizzish(n, fizz_number):
            print('fizz')
        else:
            print(n)
        n += 1
