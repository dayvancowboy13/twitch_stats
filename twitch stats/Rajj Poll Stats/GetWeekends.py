from datetime import date, timedelta

day = date(2019,4,22)
oneDay = timedelta(days=1)

print("Starting date: ", day)

#### test to see how casting the date object to a string looks
#strDay = str(day)

#print("String of the date object: " + strDay)
####

weekendDates = []

# loop through the days since January 1st of this year until today,
# check if the day is a weekend (sat = 6, sun = 7) and if so
# add date to a list
while(day.year == 2019 and day != date.today()):

    if (day.isoweekday() == 6 or day.isoweekday() == 7):
        weekendDates.append(day)
        day += oneDay
    else:
        day += oneDay
        continue


f = open('weekend_dates.txt', 'w')

for entry in weekendDates:
    f.write(str(entry)+'\n')

f.close()
