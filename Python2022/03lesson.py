name = 'Irina'
print('Heloo',name)
# This is a comment
print('Irina')

string_sample = "Hello world world"
string_sample2 = "first letteR is lowErcase"
string_sample3 = " extra whitespace string"
german_sample = "der Fluẞ"

sample = '''Hello
Irina
Planet'''
print(sample)


print(len(string_sample))


print(string_sample[16])


print(string_sample[-5:])
# -5 обратный отчет
# -5:

sample = "hello"

print("hello" in string_sample)
# hello net s mal bukvi budett  False, mogut bit peremennie



print(string_sample[0:5] + " Irina")

hello_string = string_sample[0:5]
print(hello_string)

hello_spl = "hello"
print(hello_spl in string_sample)

print(string_sample.upper())
#zaglavnie bukvi

print(string_sample.upper())

string_sample = string_sample.upper()
print(string_sample)


print(german_sample.lower())
# napisano kak est'
print(german_sample.casefold())
# peredelaet v standart

helo_spl = "hello"

print(german_sample.lower())
print(german_sample.casefold())
print(german_sample[5:12].upper())
print(helo_spl.capitalize()) # delaet pervoe slovo s zaglavmoi bukvoi

print(string_sample3.strip())
#obrezaet probeli
.lstrip  #sleva
.rstrip    #SPRAVA

print(string_sample.replace("world", "planet"))
# zamena slova

print(string_sample.replace("world", "planet",1))
# zamena  pervogo slova


print(string_sample.split())
#razbivael stroku na slova

a, b, c = string_sample.split()

print(a)
print(b)
print(c)
#razbivaet po kolli4estvu peremennih

a, b, c = input("Please enter something").split()

print(a)
print(b)
print(c)

#vnizu pi6e6 4to razdelit na 4asti i  4to bratza delitel

print(string_sample.find('world', 7, 10))
#i6et sovpadeniaj


print(string_sample.find('world'))
print(string_sample[string_sample.find('world'):])


print(string_sample.find('world'))
print(string_sample[string_sample.find('world'):(string_sample.find('world') + len('world'))])
print(string_sample[6:11])

x = "123456789098765"
print(len(x))
#izmerit kolli4estvo  v stroke

print(string_sample.count('world'))
#pos4etaet skolko raz bilo slovo

a = "Hello"
b = "world"
print(a + ' ' + b)  #slozenie
print(a, b, 'planet')   # PERE4ESLENIE

salary = 2000
first = 'Bob'
last = 'Smith'  #True - vsjo ravno postavit stroki
sample = 'Helli {} {}. Your salary is {}'
print(sample.format(first, last, salary))

salary = 2000
first = 'Bob'
last = 'Smith'
sample = 'Helli {2} {1}. Your salary is {0}'
print(sample.format(first, last, salary))


salary = 2000
first = 'Bob'
last = 'Smith'
sample = 'Helli {0} {1}. Your salary is {0}. Is your name {3}'
print(sample.format(first, last, salary, 'London'))

a = 1000
b = 'computer'
print('This is {product:}. It costs {price:}.'.format(product=b, price=a))



x = 12354.335546456151321
y = 613.2689
print('The value of x is %.4f' % x)
print('The value of x is %.2f' % x)

#ustarev5ii metod
emp_name 'John'
emp_age = 30
emp_salary = 1500

emp_string = 'Hi, my name is %(name)s! I am %(age)s olg. My salary is'\
    '%(salary).2f' % {'name': emp_name, 'salary': emp_salary, 'age': emp_age }
print(emp_string)

salary = 2000
first = 'Bob'
last = 'Smith'
sample = 'Helli {0} {1}. Your salary is {0}. Is your name {3}'
print(sample.format(first, last, salary, 'London'))
print(f'Hello {first} {last}. Your salary is {salary}') # f - formatirovannaja stroka

print(f'Hello {first.upper()} {last.upper()}. Your salary is {salary:.2f}')
print(r' \n Hello World') #r siraja stroka, v nei ni4ego ne proishodit . nikakih komand ,
# esli ne nado 5tobi 4to-to ne vosprinimala sistema


byte_string = b' '  # unicode-table.com можно найти иероглифы
print(byte_string.decode( ))

!!!!!
a = 1000
b = 'John'
c = 30

print(f'Hi, my name is {b}. I am {c}.My salary is {a} euro.')
#F formatirovannaja stroka



x = 5
print(x)

x += 1  #pribavit 4islo
print(x)

x = x + 1
print(x)




sample_string =  'hello'
sample_string2 =  'Hello \'world\''

print(sample_string2)

# \n perenos stroki                  \\n  perenesjot tekst s sleshom
# \t tabuljatsija ili 4 probela
# \b backspace
# 'Hello \'world\''    that\'s       ostavit kavi4ki



sample_string3 = """
FGF
DGfg
fgdhg
dfgh
"""
print(sample_string3)
# perenesjot luboi tekst esli ego stavit v 3 """


