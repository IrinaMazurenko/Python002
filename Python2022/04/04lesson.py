#LIST
# SPLIT metodi dlja pustogo spiska

# objavlenie pustogo spiska
empty_lst = []
print(type(empty_lst))

#sozdanie tipa dannih iz stroki, kazdoe slovo stanovitsja otdelnim elementom
empty_lst = 'Hello world'.split()
print(empty_lst)
print(type(empty_lst))

#vidast pustoi spisok
empty_lst = list()  # ili []
print(empty_lst)
print(type(empty_lst))

#spisok v nem mozet bit mnogo 4ego i s6e spisok
world = 'world'
filled_lst = ['hello', world, 1023, 0.2596,True, False, None, [1, 2, 3, ]]
print(filled_lst)

#pi6et kolli4estvo slov
courses = ['Histroty','Math','Literature','Psysics','Programming']
print(len(courses))
print(len(filled_lst))

#vividet slovo ili tsifru
courses = ['Histroty','Math','Literature','Psysics','Programming']
print(len(courses))
print(len(filled_lst))
print(courses[0]) # histiry eto 0 ,,,,,,[4], [1:3]  [::-1]-spisok v obratnom porjadke

# mozno indeksirovat
filled_lst = ['hello', world, 1023, 0.2596,True, False, None, [1, 2, 3, ['one','two','three'],4], 'world']
print(filled_lst[-2][2])

#zamena
courses = ['Histroty','Math','Literature','Psysics','Programming']
courses[0] = Art   #ili [0:3] srez iz spiska
print(courses)

#
courses = ['Histroty','Math','Literature','Psysics','Programming']
print(len(courses))
print(filled_lst[-2][2])
numbers = [1, 5, 6, 8, 3, 4, 2]
print(courses[4])
courses[0:3] = [1, 2, 3, 4, 5, 6, 7]
print(len(courses))
print(courses[4])
print(courses)

#append
# dobavljaet novi eliment na konets spiska
# ego ne vivodjat na print, tk buded None
courses = ['Histroty','Math','Literature','Psysics','Programming']
print(courses)
courses.append('ART')
print(courses)
#insert
#zamenjaet opredelenni element
courses.insert(1, 'English')
print(courses)
#extend
#raz6iret spisok, dobavit
courses2 = ['Art', 'English']
courses.extend(courses2)
print(courses)

# udalenie
#remove
#rabotaet s pervim naidennim elementom( nuzno zna4enie)
courses.remove('Art')

#pop
# udaljaet posledni element (mozno udalit po indeksu
x = courses.pop(2)
print(courses)
print(x)
print(courses.pop()) # vidaet udaljonnii element

#reverse
#sohranaet v obratnom porjadke
courses.reverse()

#sort
# sortiruet odinakovie stroki po table unicode
courses = ['Histroty','Math','Literature','Psysics','Programming','1', '5', '6', '8', '3', '4', '2']
numbers = [1, 5, 6, 8, 3, 4, 2]

print(courses)
courses.sort()
print(courses)

#sort.reverse
#sortiruet v obratnom porjadke po unicode
numbers = [1, 5, 6, 8, 3, 4, 2]

print(courses)
numbers.sort(reverse = True)
print(numbers)

#sorted
print(sorted(courses)) #

#statisti4eskie metodi

print(min(numbers)) #esli ispolzovat k slovam, to viberit po unicode
print(max(numbers)) #esli ispolzovat k slovam, to viberit po unicode
print(sum(numbers)) #summa

# poisk po spisku, polnostju povtorit element
print(courses.index('Math'))

#naidet element v spiske
courses = ['Histroty','Math','Literature','Psysics','Programming','1', '5', '6', '8', '3', '4', '2']
print('Math' in courses)

# join, obratni split(udoljaet)
# sobiraet v stroku i dobavljaet delitel
courses = ['Histroty','Math','Literature','Psysics','Programming','1', '5', '6', '8', '3', '4', '2']
courses_str = ', '.join(courses)
print(courses_str)
print(type(courses_str))

#kopija spiska
courses2 = courses.copy() # kopiruet peremennuja

#count
print(courses.count('Math')) # s4etaet skolko ra4 zna4enie est v spiske



!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# TUPLE kortez
#ispolzuetsja 4tob izbavitsja ot dublikatov

empty_lst = (1,) # zapjatala pokazet i skobki
print(empty_lst)
print(type(empty_lst))

# povernut s pomo6ju indeksatsii
courses = ['Histroty','Math','Literature','Psysics','Programming','1', '5', '6', '8', '3', '4', '2']
numbers = [1, 5, 6, 8, 3, 4, 2]

courses = courses[::-1]
print(courses)

# vsego 2 metoda k kortezu
#.count  s4itaet skolko raz vstretsjaetsja v karteze
#.index   na kakoi pozitsii zna4enie nahoditsja


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#SET
# ne uporjadotseno
empty_lst = {1}
print(empty_lst)
print(type(empty_lst))


courses = {'Histroty','Math','Literature','Psysics','Programming','1', '5', '6', '8', '3', '4', '2'}
numbers = {1, 5, 6, 8, 3, 4, 2}


print(courses)
print(numbers)
print(len(courses))
#ne vivedet dublikati
# ne slozit slova i tsifri
 # .remove udalit pervi pohozi element( ne sohranit udaljonnoe znatsenie)
 # .pop net orgumeta v skobke, sohranit,udoljaet vsjegda raznie elementi, v sju4ae 4isla udoljaet naimen6ee 4islo
 # .add dobavit element
 # .copy
 #. clear udalit
 # .update (extend dlja list )



 #.intersection nahodit ob6ee
set1 = {'Histroty','Math','Literature','Psysics'}
set2 = {'Programming','Art','Design','History'}
print(set1.intersection(set2))

#.difference
print(set1.difference(set2))  4em set1 otli4aetsja ot set2 ili naoborot

#.issubset
print(set1.issubset(set2))  javljaetsja li set1 4astju set2
#.issuperset
print(set1.issuperset(set2)) javljaetsja li set1 setom soderzasemsja v set2
#union
print(set1.union(set2))  soedinit 2 seta
#set ne konventiruetsja v int  i float

#bool vozvrja6aet False

# spisok v koto4om udalilis dublikati, ne uporjado4en
sample_list = ['One','Two','Two','three']
print(list(set(sample_list)))