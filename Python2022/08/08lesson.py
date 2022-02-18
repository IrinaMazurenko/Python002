# r - read
# a - append   # doballjae toze samoe 4to uze est' # dopolnit fail esli ego net
# w - write    # dopolnit fail esli ego net
# x - create   # dlja odnogo raza создаст файл , но если 2ой раз то не будет создавать
# r+ = read and write   # otkrit, 4itat ,dopolnjat', no ne perezapisivT'

# file = open('TExt_files/lorem.txt', 'r', encoding='utf-8')
# print(file)                     # vivodit fail v pe4at
# print(file.name)                # put k failu
# print(file.mode)                # rezim
# print(file.encoding)            # kodirovka

# print(file.closed)              # proverka javljaetsja li fail zakritim
# file.close()                    # zakrivaet fail
# print(file.closed)

#
# with open('TExt_files/lorem.txt', 'r', encoding='utf-8') as file:  # pozvoljaet avtomatom zakrit' fail
#     print(file.closed)
# print(file.closed)

#
# with open('TExt_files/lorem.txt', 'r', encoding='utf-8') as file:
#     file_content = file.read()  # read sohranjaet vse perenosi strok kak v originale # (50) - skolko mozno pro4itat simvolov
#                                  # 4itaet odin raz
#     file.seek(0)  # pro4itat' 2oi raz, esi vvest 50 pro4itaet do 50 znaka
#     file_content2 = file.read()
#     print(file_content2)

# with open('TExt_files/lorem.txt', 'r', encoding='utf-8') as file:
#     file_content = file.readline(100)    # 4itaet stroku
#     file_content2 = file.readline()
#     print(file_content)
#     print(file_content2)
#
# with open('TExt_files/lorem.txt', 'r', encoding='utf-8') as file:
#     file_content = file.readlines(1)    # vozvra6aet spisok, element eto stroka
#     file_content2 = file.readlines()
#     print(file_content)
#     print(file_content2)

# print('Hello', end='Line end \n')    # otmenjaet perenos stroki
# print('world')

# with open('TExt_files/lorem.txt', 'r', encoding='utf-8') as file:
#     for line in file:   #
#         print(line)
#
#
# with open('TExt_files/lorem.txt', 'r', encoding='utf-8') as file:
#     chunk_size = 100         # sdelaet v stroke 100 simvolov
#     file_content = file.read(chunk_size)
#     while len(file_content) > 0:
#         print(file_content)
#         file_content = file.read(chunk_size)
#     file.write('TEST')                            #esti read , to pisatä v nem nelzja


# with open(f'TExt_files/test{num}.txt', 'x') as file:    {}
#   file.write('HEllo world')



# with open('TExt_files/test.txt', 'w') as file:
#   file.write('Hello world 111 2222222222 ')
#   file.seek(5)
#   file.write('Hello World')  # eto vstavi tposle 5ogo simvola

# with open('TExt_files/test.txt', 'r') as file:
#   with open (''TExt_files/test.txt', 'w'') as wfile:
#     for line in file:
#       wfile.write(line)



with open('TExt_files/python.jpg', 'rb') as file:   # otkritie foto  +'rb'
     with open('TExt_files/python.jpg', 'wb') as wfile:
       chunk_size = 4096                                  # baiti
       file_chunk = file.read(chunk_size)
       while(len(file_chunk)) > 0:
       wfile.write(file_chunk)
       file_chunk = file.read(chunk_size)



