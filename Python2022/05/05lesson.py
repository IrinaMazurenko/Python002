!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#DICTIONARY
#ne razre6aet dublikatov
x = 5
student = {}   #dict ili {}
print(type(student))

student = {'name': 'Jack', 'age': 32,'courses': ['Math', 'Art', 'Programming'],
           1: 'int key', 0.2: 'float ket', x: 'variable', 'variable': x}

#indeksiruetsja po klu4u

# .get
# za6ita ot o6ibok v kode\
print(studednt.get('job', True)) #4erez , 4to vozvratit

#print(type(studednt.get('job', True))) #4erez , 4to vozvratit
# True -bool
# 1,2,3 - list

#.update zamenit i dobavit to 4to net
print(student)
student.update({'name': 'Mary','age': 25, 'job': "Programmer"})
print(student)

#del udoljaet 4to-to
del student['another_name'] #udalit vse varianti


#.pop udoljaet posledni element
#ne mozet bit pustoi
# 'age': 32 udalit zna4enie no ne tsizru

x = [1, 2, 3]
y = x.pop()
print(y)

#.copy
student2 = student.copy()

#.popitem
# udoljaet uslovno posledni element
x = student.popitem()
print(x)
print(student)


#for vivodit klu4i, ne zna4enija
x = 5
student = {'name': 'Jack', 'age': 32,'courses': ['Math', 'Art', 'Programming']}

for x in student:
    print(x)
 # tak vivesit  zna4enija
 print(student[x])
#vivedit kak spisok
print(list(student.keys())


print(student.keys() # vivodit klu4i
print(student.values()) # vivodit zna4enija
  # ili....
  # for x in student.values
  #  print(x)
print(student.items()) # vivodit klu4 i zna4enie

for key, value in student.items():
    print(key,value)

!!!!!!!!!!!!!!!!!!!!!
#beskone4ni,
while True:
    print('Ican\'t stop!')

#
x = 0
while x < 10:
    print(x)
    x += 1





!!!!!!!!!!!!!!!!!!
#WHILE
distance_to_target = float(input('Please enter distance in km:'))
current_position = 0

step = 0.6
step_cnt = 0
distance_in_meters = distance_to_target * 1000

while current_position < distance_in_meters:
    print(step_cnt)
    current_position += step
    step_cnt += 1
    print('Step to walk ' + str(step_cnt))



#pass
x = 100

if x > 0:
    pass  #idnor, uslovija vipolneni no vivod ignoritjja
elif x < 0 :
    pass

#break
#slomat, razorvat



#continue
# razorvjot konkretni krug tsikla



try: # v nem pi6etsja kod kotori mozit vizvat o6ibku, esli o6ibka idjot v except
    int('sdfgadfgd')
except:
    print('ERROR')


try: # v nem pi6etsja kod kotori mozit vizvat o6ibku,esli net o6ibki idet v else
    int('1225665')
except:
    print('ERROR')
else:
    print('oK')

###
try:
    int('1225665')
except:
    print('ERROR')
else:
    print('oK')    # ne objazatelno
finally:
    print('Good bye') # pi6etsja v lubom slu5ae # ne objazatelno

####
x = [1, 2, 3]
try:
    # int('dfgdhh')
    print(x[10])
except ValueError:  #opisivaet opredelejonnuju o6ibku
    print('ERROR')
except IndexError:  #opisivaet opredelejonnuju o6ibku # mozet bit mnogo
    print('ERROR')
else:              # ne objazatelni
    print('oK')
finally:           # ne objazatelni
    print('Good bye')

