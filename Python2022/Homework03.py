# 0-100
# Если число делится на 3 без остатка - написать число и Fizz
# Если число делится на 5 без остатка - написать число и Buzz
# Если число делится на 3 и на 5 без остатка - написать число и FizzBuzz


sample = list(range(0,101))


for num in sample:
    print(num)
    if num % 3 ==0:
        print(num,'Fizz')
    if num % 5 ==0:
        print(num,'Buzz')
    if num %2 == 0 and num % 5 ==0:
        print(num,'FizzBuzz')


