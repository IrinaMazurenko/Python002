import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaH
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc

ball mall hall wall tall
'''
sentence = 'Start a sentence and then bring it to an end Start'


pattern = re.compile(r'M(rs|s|r)\.? [A-Z][a-z]*')                # ()group rs-bol6e ,ee v na4alo  *-. est' ili net ?-0 ili 1

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match.group(2))



# # str1 = r'\tab'    r' vivedet siroi tekst
# # print(str1)
#
# pattern = re.compile(r'[1-5]')
#
#
# matches = pattern.finditer(text_to_search)
# # matches = pattern.finditer(sentence)
#
# for match in matches:
#     print(match)
#
#
#
#     # print(match.start())
#     # print(match.end())
#     # print(match.group())
#
#
#
# # print(text_to_search[1:4])
# # print(text_to_search[270:273])