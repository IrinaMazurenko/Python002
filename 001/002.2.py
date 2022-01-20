a = 500
b = 45.5

print(5 + 5 - 1)
print(a / 44)
print(a // 5)

print(a % 4)

print(3 ** 2)


# Tris is a comment
a = 400 #int()
b = 45.5 #float()
c = True #bool()
d = None
e = 'Hello world' # str()

print

name = input('What is your name?')
lastname = input('Enter lastname:')
age = input('Enter age:')
print(type(age))

print('Hello', name, lastname + '! You are', age, 'years old!')
print('Hello ' + name + ' ' + lastname + '! you are ' + age + ' years old!')
print('Hello',True, None, 100, 12.236)

# Ask user to enter sides of a triangle
side_a = float(input('Enter side A: '))
side_b = float(input('Enter side B: '))
side_c = float(input('Enter side C: '))

# Find half perimetr
half_perimetr = (side_a + side_b + side_c) / 2
triangle_area = (half_perimetr * (half_perimetr - side_a) *\
                (half_perimetr -side_b) * (half_perimetr - side_c)) ** 0.5
print("Area of a triangle is", triangle_area)