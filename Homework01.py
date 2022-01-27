#1. Высчитывает возраст из заданых данных (current_year - нынешний год, year_of_birth - год рождения)
current_year = 2022
year_of_birth = 1988
print("You are", current_year - year_of_birth, 'years old')


# code parts
code_1 = '354'
code_3 = 132

# code 2 data
x = 152
y = 132


#2. Code_2
# a. найдите остаток от x деленого на y
print('Остаток от x деленого на y равен ',(x % y))

#b. полученый результ умножте на 13
factor = (x % y) * 13
print("Если полученый результат умножить на 13,то получится", factor)

#c. извлеките квадратный корень из полученного результата
square_root = factor ** 0.5
print('Квадратный корень из полученного результата', square_root)

#d. возьмите целую часть от результа
full_square_root = int(square_root)
print("Целая часть от результа равна", full_square_root)

# 3. Соединить код в отдельную переменную
code = code_1 + "-" + str(int(full_square_root)) + "-" + str(code_3)
print(code)


# 4. Вывести строку:

name = "Mary"
lastname ="Gold"
sample = 'Hello {} {}.'
print(sample.format(name,lastname),"You are", current_year - year_of_birth, 'years old.', 'Your secret code is', code )

# CORRECTION
age = current_year - year_of_birth
code_2 = int(((x % y) * 13) ** 0.5)
secret_code = f'{code_1}-{code_2}-{code_3}'
print(f'Hello {name} {lastname}. You are {current_year - year_of_birth} years old. Your secret code is {secret_code}')