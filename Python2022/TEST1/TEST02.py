# a = float(input("Enter side A: "))
# b = float(input("Enter side B: "))
#
# sqrt = a*a + b*b
# print(sqrt)
#
# c = sqrt ** 0.5
# print(c)


#CORRECTION
side_a, side_b= input('Please enter side A and side B. Use ", " as separator: ').split(', ')

print(f'Side C is {float(side_a)  ** 2 + float(side_b) ** 2 ** 0.5:.2f}')
print(math.sqrt(25))