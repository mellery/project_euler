def problem19():
    day = 1
    month = 1
    year = 1901
    date = 2
    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    
    ans = 0

    while (day <= 31 and month <= 12 and year <= 2000):
    #for x in range(0,100):
        leapyear = False
        if (year % 4 == 0) and year != 1900:# and (year % 100 == 0 and year % 400 != 0):
            leapyear = True

        #print(day,month,year,days[date],leapyear)

        if (day == 1 and days[date] == 'sunday'):
            print(day,month,year,days[date],leapyear)
            ans = ans + 1

        day = day+1
        date = date + 1
        if date >=len(days):
            date = 0

        if month in [2]:
            if leapyear and day > 29:
                day = 1
                month = month + 1
            elif day > 28:
                day = 1
                month = month +1

        if month in [9,4,6,11]:
            if day > 30:
                day = 1
                month = month + 1
        else:
            if day > 31:
                day = 1
                month = month + 1
        if month > 12:
            month = 1
            year = year + 1
        #elif month in [2]:
        #    if day > 28 and year%4

    return ans

print(problem19())