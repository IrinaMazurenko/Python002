#Создать запрос для определения в тексте цифр,
# за которыми не стоит знак +. (Примеры выражений “2*9-6*5” или (3+5)-9*4)

import re

text_to_search = '''
2*9-6*5
(3+5)-9*4
'''

pattern = re.compile(r'\d[^\+]')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)