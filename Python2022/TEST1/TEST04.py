#
# list = input('Enter your list items separate by commas ')
# print(str(list))
# list.reverse()
# print(list)
#
#


#CORRECTION
# user_input = input('Enter your list items separate by commas ').split(', ')
# user_input.reverse()
# for element in user_input:  # vivedet po strokam
#     print(element)


#CORRECTION  2
user_input = input('Enter your list items separate by commas ').split(', ')
for element in reversed(user_input):
    print(element)

