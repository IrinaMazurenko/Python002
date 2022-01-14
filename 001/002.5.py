# Ask user to enter sides of a triangle
side_a = float(input('Enter side A: '))
side_b = float(input('Enter side B: '))
side_c = float(input('Enter side C: '))

# Find half perimetr
half_perimetr = (side_a + side_b + side_c) / 2
triangle_area = (half_perimetr * (half_perimetr - side_a) *\
                (half_perimetr -side_b) * (half_perimetr - side_c)) ** 0.5
print("Area of a triangle is", triangle_area)