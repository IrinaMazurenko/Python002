people = [
    ('Jack', 'Smith', 25, 'Male'),
    ('Mary', 'Gold', 18, 'Female'),
    ('Sarah', 'Connor', 32, 'Female'),
    ('Piere', 'Summers', 45, None)
]

for person in people:
    if person [3] == 'Male':
        print(f'This is {person[0]} {person[1]}. He is {person[2]} years old.')
    elif person[3] == 'Female':
        print(f'This is {person[0]} {person[1]}. She is {person[2]} years old.')

for name, surname, age, gender in people:
    if gender == 'Male':
        print(f'This is {name} {surname}. He is {age} years old.')
    elif gender == 'Female':
        print(f'This is {name} {surname}. She is {age} years old.')
    else:
        print(f'This is {name} {surname}. It is {age} years old.')