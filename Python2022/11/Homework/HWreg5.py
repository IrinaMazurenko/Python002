# Написать регулярное выражение для проверки строки,
# задача определить состоит ли строка из символов a-z, A-Z, 0-9.

import re

text_to_search = '''
236548695AJDKf.,ggjGGG
56965
fgdfg
FGHJKL
'''
pattern = re.compile(r'[a-zA-Z0-9]')

matches = pattern.match(text_to_search)

print(matches)