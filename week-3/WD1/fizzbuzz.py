i = 0

while i <= 100:

    if (i % 3 == 0) and (i % 5 == 0) or ("3" in str(i) and "5" in str(i)) or (i % 3 == 0 and "5" in str(i)) or (i % 5 == 0 and "3" in str(i)):
        print ('fizzbuzz')

    elif i % 3 == 0:
        print ('fizz')

    elif i % 5 == 0:
        print ('buzz')


    elif "3" in str(i):
        print ('fizz')

    elif "5" in str(i):
        print ('buzz')

    else:
        print (i)
    i += 1
