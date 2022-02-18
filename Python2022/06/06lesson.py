#DEF aeyrwbb


def squeares():
    print('Hello world')

squeares()   #skolko raz povtorit stolko i viidet

def double(x):
    x = 10
    return x   #  prekra6aet svoju rabotu  # funktsija stanovitsja tem 4to v return
print(double())  !!!!!!!!!



squeares()
print(double())
print(x)


# если переменные внутри функции то они там и остаются
# если снаружи функции, то внутри можно к ним обращаться

def squeares(number):   # vnutri funktsii uslovie, k kotoromu nuzna peremennaja
    return number ** 2

print(squeares(25))        # 25*25=625


#
def squeares(number, x, y, z):   # kod vnutri funktsii mozet bit bol6oi
    result = x * y * z
    result -= numbers
    return result

def double(number):
    return number * 2

def tripple(number):
    return nember  * 3

x = 15
y = 20
z = 25

print(double(x))        #beret iz double i * )x) 15


def fizzbuzz(start_num, stop_num):
    for num in range(start_num, stop_num + 1):
        if num % 3 == 0 and num % 5 == 0:
            if num % 100000 == 0:
                print(num, 'FizzBuzz')
        elif num % 3 == 0:
            if num % 100000 == 0:
                print(num, 'Fizz')
        elif num % 5 == 0:
            if num % 100000 == 0:
                print(num, 'Buzz')

