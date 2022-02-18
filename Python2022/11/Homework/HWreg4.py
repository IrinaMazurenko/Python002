#Написать программу котороая будет выбирать из файла people.txt:
#	1) Все имена и фамилии
#	2) Все адреса

import re
with open('people.txt', 'r', encoding='UTF8') as file:
    people_data = file.read()


pattern = re.compile(r'([A-Z][a-z]+) ([A-Z][a-z]+[^\s.\-,CityPark])')
matches = pattern.finditer(people_data)
# print(len(list(matches)))
for match in matches:
    print(match)