#CORRECTION

# tuple1 = (1, 2, 3, 5, 8)
# tuple2 = (8, 2, 5)
# tuple3 = tuple1[:2]  + tuple2 + tuple1[2:]
# print(tuple3)
# print(type(tuple3))


#CORRECTION2
# tuple1 = (1, 2, 3, 5, 8)
# tuple2 = (8, 2, 5)
#
# tuple1 = list(tuple1)
# for num in tuple2[::-1]:
#     tuple1.insert(2, num)
#
# tuple1 = tuple(tuple1)
# print(tuple1)

#CORRECTION3
tuple1 = (1, 2, 3, 5, 8)
tuple2 = (8, 2, 5)
tuple1 = list(tuple1)
tuple1.insert(2, tuple2[2])
tuple1.insert(2, tuple2[1])
tuple1.insert(2, tuple2[0])
