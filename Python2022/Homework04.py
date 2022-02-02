while True:
    isikukood = input('Please enter your ID or type Exit:')
    if isikukood.lower() == 'Exit':
          print('Goodbye!')
          break
    else:
          try:
              int(isikukood)
              if len(isikukood) != 11:
                  raise UserWarning
          except ValueError:\
              print('ID you entered is not numeric!')
          except UserWarning:
              if len(isikukood) > 11:
                  print('ID is too long')
              else:
                  print('ID is too short')
              continue
          else:
              if isikukood[0] == '1':
                 bcent = '18'
                 gender = 'Male'
              elif isikukood[0] == '2':
                 bcent = '18'
                 gender = 'Female'
              elif isikukood[0] == '3':
                 bcent = '19'
                 gender = 'Male'
              elif isikukood[0] == '4':
                 bcent = '19'
                 gender = 'Female'
              elif isikukood[0] == '5':
                 bcent = '20'
                 gender = 'Male'
              elif isikukood[0] == '6':
                 bcent = '20'
                 gender = 'Male'
              else:
                 bcent = 'Unknown'
                 gender = 'Unknown'


# code_1 = isikukood[0]
#
# first_number = [('1', '1800 - 1899', 'mees'),
#                 ('2', '1800 - 1899', 'naine'),
#                 ('3', '1900 - 1999', 'mees'),
#                 ('4', '1900 - 1999', 'naine'),
#                 ('5', '2000 - 2099', 'mees'),
#                 ('6', '2000 - 2099', 'naine'),
#                 ('7', '2100 - 2199', 'mees'),
#                 ('8', '2100 - 2199', 'naine')]
#
# for code_1, year, gender in first_number:
#     if code_1[0] == isikukood[0] == '1':
#         print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')
#     elif code_1[0] == isikukood[0] == '2':
#         print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')
#     elif code_1[0] == isikukood[0] == '3':\
#         print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')
#     elif code_1[0] == isikukood[0] == '4':\
#         print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')
#     elif code_1[0] == isikukood[0] == '5':\
#         print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')
#     elif code_1[0] == isikukood[0] == '6':\
#         print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')
#     elif code_1[0] == isikukood[0] == '7':\
#         print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')
#     elif code_1[0] == isikukood[0] == '8':\
#         print(f'Sinu kood algab {code_1[0]}, sinu sünniaeg {year} ja sina oled {gender}.')


              byear = isikukood[1:3]
              bmonth = isikukood[3:5]
              bday = isikukood[5:7]

# print(isikukood[1:3], '- see on sinu sünniaeg')
# print(isikukood[3:5], '- see on sinu sünnikuu')
# print(isikukood[5:7], '- see on sinu sünnipäev')

# print(isikukood[7:10], 'need numbrid näitavad kus sa olid sündinud')
# code_2 = int(isikukood[7:10])
# print(int(isikukood[7:10]))


              if int(isikukood[7:10]) in range(1, 11):
                  region = 'Kuressaare haigla'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(11, 20):
                  region = 'Tartu Ülikooli Naistekliinik'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(21, 151):
                  region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(151, 161):
                  region = 'Keila haigla'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(161, 221):
                  region = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(221, 271):
                  region = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(271, 371):
                  region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(371, 421):
                  region = 'Narva haigla'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(421, 471):
                  region = 'Pärnu haigla'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(471, 491):
                  region = 'Haapsalu haigla'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(491, 521):
                  region = 'Järvamaa haigla (Paide)'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(491, 521):
                  region = 'Järvamaa haigla (Paide)'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(521, 571):
                  region = 'Rakvere haigla, Tapa haigla'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(571,601):
                  region = 'Valga haigla'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(601,651):
                  region = 'Viljandi haigla'
                  print('Sinu sünnikoht on', region)
              elif int(isikukood[7:10]) in range(651,700):
                  region = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
                  print('Sinu sünnikoht on', region)
              else:
                  region = 'Unknown'

              while True:
                  user_menu = input('Please choose:\n1.Tell gender:\n'
                                    '2.Tell date of birth\n'
                                    '3.Tell birth region\n'
                                    '4.VAlidate ID\n'
                                    '5.Change ID\n'
                                    '6.Exit\n-->')
                  if user_menu == '1':
                    if gender != 'Unknown':
                        print(f'Gender: {gender}')
                    else:
                        print('Impossible to determine gender.')
                  elif user_menu =='2':
                      if bcent != 'Unknown':
                         print(f'DOB: {bday}.{bmonth}.{bcent + byear}')
                      else:
                          print('Impossible to determine date of birth')
                  elif user_menu == '3':
                      if region != 'Unknown':
                          print(f'You were born id {region}')
                      else:
                          print(f'You were not born in Estonia')
                  elif user_menu == '4':
                      astme_kaal1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
                      astme_kaal2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
                      result = 0
                      index_cnt = 0
                      for num in astme_kaal1:
                          result += num * int(isikukood[index_cnt])
                          index_cnt += 1
                      if result % 11 == int(isikukood[-1]):
                              print('ID is valid')
                      else:
                        result= 0
                        index_cnt = 0
                        for num in astme_kaal2:
                            result += num * int(isikukood[index_cnt])
                            index_cnt += 1
                        if result % 11 == int(isikukood[-1]):
                            print('ID is valid!')
                        else:
                            print('ID is invalid!')
                  elif user_menu == '5':
                      break
                  elif user_menu == "0":
                      print('Good bye')
                      quit()
                  else:
                      print('Choice is out of range')




