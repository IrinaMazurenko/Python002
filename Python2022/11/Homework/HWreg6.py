# Написать регулярное выражение для определения эстонского личного кода (isikukood)

import re

text_to_search = '''
48512080282
'''

pattern = re.compile(r'[1-6]\d[00-99]{2}[01]\d[0-9]')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)