
def fizzbuzz(num_range):
    for num in num_range:
        if num % 5 == 0 and num % 3 == 0:
            print(num, 'FizzBuzz')
        elif num % 3 == 0:
            print(num, 'Buzz')
        elif num % 3 == 0:
            print(num, 'Fizz')
