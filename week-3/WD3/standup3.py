def is_fizz(number):
    return number % 3 == 0 or '3' in str(number)

def is_buzz(number):
    return number % 5 == 0 or '5' in str(number)


def fizz_buzz(minimum, maximum = 100):
    n = minimum
    while n <= maximum:
        if is_buzz(n) and is_fizz(n):
            print('fizzbuzz')
        elif is_buzz(n):
            print('buzz')
        elif is_fizz(n):
            print('fizz')
        else:
          print(n)
        n += 1

fizz_buzz(1, 100)
