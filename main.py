import calendar


print(calendar.weekheader(3))
#print()
#print(calendar.firstweekday())
#print(calendar.month(2020,9,w=3,l=3))
#print(calendar.monthcalendar(2020,9))
print(calendar.calendar(2020))

day_of_the_weekday = calendar.weekday(2020,9,11);
print(day_of_the_weekday)

is_leap = calendar.isleap(2020)
print(is_leap)