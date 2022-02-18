#Найти в тексте время. Время имеет формат часы:минуты. И часы, и минуты состоят из двух цифр, пример: 09:00.
# Напишите регулярное выражение для поиска времени в строке: «Завтрак в 09:00».
# Учтите, что «37:98» – некорректное время.

import re

text_to_search = '''
Завтрак в 09:00
23:59
37:98
'''

pattern = re.compile(r'(([0-1]\d|2[0-3]):[0-5]\d)')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)