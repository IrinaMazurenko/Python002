
import re

emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk.co.uk
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
'''
#emails
# pattern = re.compile(r'[\w.-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]+')
# matches = pattern.finditer(emails)
# for match in matches:
#     print(match)

#urls
pattern = re.compile(r'(http://|https://)?(www\.)?([A-Za-z0-9-]+)\.([A-Za-z0-9]+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(1, 2, 3, 4))

sentence = 'Start a sentence and then bring it to an end Start'
#sub
#matches = patterb.sub(r'\2\3\4', urls)           # vivedet gruppi, te stroka s rezultatami
#print(matches)

#findall   spisok sovpadenii
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# mathes = pattern.findall(text_to_search)

#match    i6et odno sovpadenie v na4ale stroki

#search    odno sovpadenie v lubom meste,      v objekte match

#fullmatch   sovpadaet vsja stroka

#split     razbivaet stroku po patternam

pattern= re.compile(r' [.!?,]? ')
matches = pattern.split(sentence)
r'.'


([\wA-Z]+[^0-9,.\d\s]) ([\wA-Z]+[^0-9,.\d\s])')

pile(r'#[\dA-F]{6}')