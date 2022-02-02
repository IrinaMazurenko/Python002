#DATETIME library

#import library

import calendar

import calendar

day = calendar.month(2022, 1, w=5, l=5) #w -6irina v probelah ; l= rastojanie mezdu strok
print(day)
print(type(day))

#ves' god
import calendar

day = calendar.calendar(2022)
print(day)

#
import calendar

day = calendar.calendar(2022, w=5, l=1,  c=2, m=4) # m - mesjatsi v stro4ku
print(day)

#
import calendar

print(calendar.weekday(2022, 2, 2))

#
print(calendar.weekday(2022, 2, 2))
print(calendar.isleap(2022)) # visokosni god 2024

#365.25 popravka na odin den'

import calendar

print(calendar.weekday(2022, 2, 2))
print(calendar.isleap(2024))
print(calendar.leapdays(2020, 2024))


#import time

time.sleep(5)
print('Hello World') # viveddet 4erez 5 sekund

#
import time

start = time.time()
print(start) # vremja kogda zapu6ena programma
#unix timestamp

#
import time

start = time.time()

time.sleep(7)

stop = time.time()

print(stop - start)

#
import time

start = time.time()

print('Hello')

stop = time.time()

print(stop - start)

#
import time

print(time.asctime())
print(type(time.asctime())) #raspisivaet god,den' i td
print(time.gmtime())
print(type(time.gmtime()))

#
import time

print(time.asctime())
print(type(time.asctime()))
time_date = time.gmtime()  #vremja po grinvi4u
print(time_date)
print(time_date[3])   # + 2)# ispravit na na6e vremja

#mestnoe vremja
import time

print(time.asctime())
print(type(time.asctime()))
time_date = time.localtime()
print(time_date)
print(time_date[0:4])

# standartni vivod 2022-02-02
import datetime

d = datetime.date(2022, 2, 2)
print(d)
print(type(d))


#segodnja
today = datetime.date.today()
print(today)

#import datetime

d = datetime.date(2022, 1, 15)
print(d)
print(type(d))


today = datetime.date.today()
print(today)
print(type(today))

print(today - d)
print(type(today - d))

#timedelta zna4enie dni
date1 + date2 = timedalta
date1 - timedalta = date2
day2 = timedalta - date1

#today = datetime.date.today()
tdelta = datetime.timedelta(weeks=54)


#today = datetime.date.today()
tdelta = datetime.timedelta(days=10)   #(weeks=10) mesjatsa
print(today - tdelta)     # + - den'

#
print(today.year)
print(today.month)
print(today.day)  # vivedet razdelno .
#mmetod
# p - svpistvo, otribut
print(today.year, today.month, today.day)


#
print(today.weekday)
print(today.isoweekday())  #den' nedeli

#
import datetime

d = datetime.time(15, 12, 56)
print(d)     #sozdast vremja

#
import datetime

d = datetime.datetime.now()
d2 = datetime.datetime.today()
print(d)
print(d2)    #vivedet teku6uju datu

#vivedet 4to ukazano v skobkah
import datetime

today = datetime.datetime.now()

d = datetime.datetime(2022, 2, 2, 15, 30, 54)
print(d.date(). #minute)

#import datetime

today = datetime.datetime.now()

d = datetime.datetime(2022, 2, 2, 15, 30, 54)
print(today)
today = datetime.datetime.today()
tdelta = datetime.timedelta(minutes=15, days=10) 3vistavit svoi porjadok/esli ne stavit to budet po svoemu porjadku
print(tdelta)

#  strftime      mozno raspisat datu
import datetime

today = datetime.datetime.now()

d = datetime.datetime(2022, 2, 2, 15, 30, 54)

print(today.strftime('%A %d %B %Y')) #iz tablitsi# mozno perenesti ili vstavit vsjo 4to ugodno

# strptime

dt_str = 'November 30, 2020'
dt_str1 = 'nov 30, 2020'

d= datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(d)  # vivedet v svoi format

#puthon ne opredeljaet jazik rus i est

dt_str = 'November 30, 2020, 18:00'
dt_str1 = '2. veebruar  30, 2020'.replace ('veebruar.'February'')

d = datetime.datetime.strptime(dt_str, '%B %d, %Y, %H:%M')

