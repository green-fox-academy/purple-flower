num = int(input("Enter a number: "))
i=0

if (num > 1):
    for i in range(2, num):
        if num % i == 0:
            print ('It is not a prime number')

        else:
            print ('It is a prime number')
