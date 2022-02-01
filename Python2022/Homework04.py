while True:
    try:
      isikukood = input('Please enter your ID(type exit to quit): ')
      if isikukood.lower() == 'Exit':
          break
      int(isikukood)
      if len(isikukood) != 11:
          if len(isikukood) > 11:
              print('ID is wrong')
          else:
              print('ID is too short!')
          raise UserWarning

    except ValueError:   #AssetionError svobodnaja o6ibka \UserWarning
        print('ID you entered is not numeric!')
    except UserWarning:
        print('ID  you entered is not 11 digits long')
    else:
        print(isikukood)
        break


code_1 = isikukood[0]

first_number = [('1', '1800 - 1899', 'mees'),
                ('2', '1800 - 1899', 'naine'),
                ('3', '1900 - 1999', 'mees'),
                ('4', '1900 - 1999', 'naine'),
                ('5', '2000 - 2099', 'mees'),
                ('6', '2000 - 2099', 'naine'),
                ('7', '2100 - 2199', 'mees'),
                ('8', '2100 - 2199', 'naine')]

for code_1, year, gender in first_number:
    if code_1[0] == isikukood[0] == '1':
        print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')
    elif code_1[0] == isikukood[0] == '2':
        print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')
    elif code_1[0] == isikukood[0] == '3':\
        print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')
    elif code_1[0] == isikukood[0] == '4':\
        print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')
    elif code_1[0] == isikukood[0] == '5':\
        print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')
    elif code_1[0] == isikukood[0] == '6':\
        print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')
    elif code_1[0] == isikukood[0] == '7':\
        print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')
    elif code_1[0] == isikukood[0] == '8':\
        print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')

print(isikukood[1:3], '- see on sinu sünniaeg')
print(isikukood[3:5], '- see on sinu sünnikuu')
print(isikukood[5:7], '- see on sinu sünnipäev')

print(isikukood[7:10], 'need numbrid näitavad kus sa olid sündinud')
code_2 = isikukood[7:10]

second_number = [range(1, 10), 'Kuressaare haigla']

for code_2, place in second_number:
    if code_2[0] == isikukood[7:10] == '1, 10':
        print(f'Sina olid sündinud {place}.')











# astme_kaal1 = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '1')
# astme_kaal2 = (3, 4, 5, 6, 7, 8, 9, 1, 2, 3)
#
# for ak11, ak12, ak13, ak14, ak15, ak16, ak17, ak18, ak19, ak10 in astme_kaal1:
#     if ak11[0] == isikukood[0]:
#         print(ak11[0] * isikukood[0])
