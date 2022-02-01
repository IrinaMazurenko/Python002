# while True:
#     try:
#       isikukood = input('Please enter your ID(type exit to quit): ')
#       if isikukood.lower() == 'Exit':
#           break
#       int(isikukood)
#       if len(isikukood) != 11:
#           if len(isikukood) > 11:
#               print('ID is wrong')
#           else:
#               print('ID is too short!')
#           raise UserWarning
#
#     except ValueError:   #AssetionError svobodnaja o6ibka \UserWarning
#         print('ID you entered is not numeric!')
#     except UserWarning:
#         print('ID  you entered is not 11 digits long')
#     else:
#         print(isikukood)
#         break
# print(isikukood[7:10])
#
# second_number = [('001:010', 'Kuressaare haigla'),
#                  ('011:019', 'Tartu Ülikooli Naistekliinik'),
#                  ('021:150', 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'),
#                  ('151:160', 'Keila haigla'),
#                  ('161:220', 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'),
#                  ('221:270', 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'),
#                  ('271:370', 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'),
#                  ('371:420', 'Narva haigla'),
#                  ('421:470', 'Pärnu haigla'),
#                  ('471:490', 'Haapsalu haigla'),
#                  ('491:520', 'Järvamaa haigla (Paide)'),
#                  ('521:570', 'Rakvere haigla, Tapa haigla'),
#                  ('571:600', 'Valga haigla'),
#                  ('601:650', 'Viljandi haigla'),
#                  ('651:700', 'Lõuna-Eesti haigla (Võru), Põlva haigla')]
#
#
# for code_2, place in second_number:
#     if code_2[0]  == '001:010':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#     elif code_2[0]  == '011:019':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#     elif code_2[0]  == '021:150':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#     elif code_2[0]  == '151:160':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#     elif code_2[0]  == '161:220':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#     elif code_2[0]  == '221:270':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#     elif code_2[0]  == '271:370':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#     elif code_2[0]  == '371:420':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#     elif code_2[0]  == '421:470':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#     elif code_2[0]  == '471:490':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#     elif code_2[0]  == '491:520':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#     elif code_2[0]  == '521:570':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#     elif code_2[0]  == '571:600':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#     elif code_2[0]  == '601:650':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#     elif code_2[0]  == '651:700':
#         print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#
#         # (range(11, 19), 'Tartu Ülikooli Naistekliinik'),
#         # (range(21, 150), 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'),
#         # (range(151, 160), 'Keila haigla'),
#         # (range(161, 220), 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'),
#         # (range(221, 270), 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'),
#         # (range(271, 370), 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'),
#         # (range(371, 420), 'Narva haigla'),
#         # (range(421, 470), 'Pärnu haigla'),
#         # (range(471, 490), 'Haapsalu haigla'),
#         # (range(491, 520), 'Järvamaa haigla (Paide)'),
#         # (range(521, 570), 'Rakvere haigla, Tapa haigla'),
#         # (range(571, 600), 'Valga haigla'),
#         # (range(601, 650), 'Viljandi haigla'),
#         # (range(651, 700), 'Lõuna-Eesti haigla (Võru), Põlva haigla')]
#
#         # elif code_2[0]  == isikukood[7:10] == range(11, 19):
#         #     print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#         # elif code_2[0]  == isikukood[7:10] == range(21, 150):
#         #     print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#         # elif code_2[0]  == isikukood[7:10] == range(151, 160):
#         #     print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#         # elif code_2[0]  == isikukood[7:10] == range(161, 220):
#         #     print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#         # elif code_2[0]  == isikukood[7:10] == range(221, 270):
#         #     print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#         # elif code_2[0]  == isikukood[7:10] == range(271, 370):
#         #     print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#         # elif code_2[0]  == isikukood[7:10] == range(371, 420):
#         #     print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#         # elif code_2[0]  == isikukood[7:10] == range(421, 470):
#         #     print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#         # elif code_2[0]  == isikukood[7:10] == range(471, 490):
#         #     print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#         # elif code_2[0]  == isikukood[7:10] == range(491, 520):
#         #     print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#         # elif code_2[0]  == isikukood[7:10] == range(521, 570):
#         #     print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#         # elif code_2[0]  == isikukood[7:10] == range(571, 600):
#         #     print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#         # elif code_2[0]  == isikukood[7:10] == range(601, 650):
#         #     print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')
#         # elif code_2[0]  == isikukood[7:10] == range(651, 700):
#         #     print(f'Sinu sünnikoha number on {code_2}. Sina olid sündinud {place}.')


s_list = [1-10]
x = list(range(1, 10))
print(x)