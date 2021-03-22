import datetime
import calendar

name=str(input('Hi there, please enter your name: '))

print('Hi ' + name + ', Nice to meet you!')

day=str(input('Please enter the day of your birthday in the format of DD: '))

print('Thank you ' +name+ ',')

m=str(input('Now enter the Month of your birthday in the format of MM Please: '))

print('Finally ' + name + ',')

year=str(input('I will need the year you are searching for in YYYY format Please: '))


date = (day + " " + m + " " +year)

print(date)

day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

birthday = datetime.datetime.strptime(date, '%d %m %Y').weekday()


print(name+ ', I believe that in ' +year+ ', your birthday falls on a ' + day_name[birthday]+ ".")

print('Would you like to view '+ m + ' ' + year + ' in calendar format? ')

format = str(input('Y for Yes, N for No: '))

year2 = int(year)
m2 = int(m)
cal=calendar.month(year2,m2)

if format == 'n' or format == 'N':
    quit()

elif format == 'y' or format == 'Y':
    print(' ')
    print(cal)
