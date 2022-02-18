

# Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF,
# то есть # и содержит затем 6 шестнадцатеричных символов.
# HASH цвета используют значения от 0 до 15, где 0-9 цифры от нуля до 9, 10-15 буквы от A-F.

import re

text_to_search = '''
#gd6598
#DF5966
#FA59F8
#056489545ABDFDA
#
'''

pattern = re.compile(r'#[\dA-F0-9]{6}')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)