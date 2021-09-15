arr_1 = [3,4,5,6]
for number in arr_1:
    number = int(number)
    n = 1
    while n >=1 and n <= number:
        if (n % 15 == 0):
            print('FizzBuzz')
        elif (n % 5 == 0):
            print('Buzz')
        elif (n % 3 == 0):
            print('Fizz')
        else:
            print(n)
        n = n + 1