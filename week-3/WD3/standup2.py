def get_fizz(number):
    if number % 3 == 0:
        return 'fizz'
    else:
        return number

def fizz_buzz(minimum, maximum):
    n = minimum
    while n <= maximum:
            print(get_fizz(n))
            n += 1

fizz_buzz(1, 50)
