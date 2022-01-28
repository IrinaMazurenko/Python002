x = 50
if x == 100:   # должен быть один   #если все верны,то система выберит ИФ , те первое условие
    # если все условия с ИФ и они все верны, то выведет все 3
    print( 'X is equal to 100')
elif x > 100:     # может не быть
    print('X is large than 100')
else:              # может быть много
    print("Good bye")

print('Hello')



x = 100

if x == 100:
    if x -20 == 81:
    print('OK')


x = 50

if x > 0 or x < 50:
    print("Condition 1 Ok").




sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for num in sample_list:
#     print(num)
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print('Odd')

for index, value in enumerate (sample_list):
    print(index)
    print(value)


print(list(enumerate(sample_list)))


# .rande
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = list(range(0, 101))
print(x) #otobrazit ot 1 do 100

#for povtoraem itteratsiju
#if

#
course = ['Art', 'Math', 'English']

for lesson in course:
    if lesson == 'Math':
        print(f'My next lesson is {lesson}')
    else:
        print(f'I hate {lesson}')


#
people = [
    ('Jack', 'Smith', 25, 'Male'),
    ('Mary', 'Gold', 18, 'Female'),
    ('Sarah', 'Connor', 32, 'Female'),
    ('Piere', 'Summers', 45, 'Male')
]

for person in people:
    if person [3] == 'Male':
        print(f'This is {person[0]} {person[1]}. He is {person[2]} years old.')
    elif person[3] == 'Female':
        print(f'This is {person[0]} {person[1]}. She is {person[2]} years old.')


#
for name, surname, age, gender in people:
    if gender == 'Male':
        print(f'This is {name} {surname}. He is {age} years old.')
    elif gender == 'Female':
        print(f'This is {name} {surname}. She is {age} years old.')