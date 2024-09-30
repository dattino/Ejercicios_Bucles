def fizz_buzz():
    #n = 0
    #while n < 100:
        #n += 1
    for n in range(100):
        if((n > 0) & ((n % 3) != 0) & ((n % 5) != 0)):
            print(n)
        elif (((n % 3) == 0) & ((n % 5) != 0)):
            print('Fizz')
        elif(((n % 5) == 0) & ((n % 3) != 0)):
            print('Buzz')
        elif(((n % 3) == 0) & ((n % 5) == 0)):
            print('FizzBuzz')


fizz_buzz()
