def add_time(start, duration, day=''):
    # split the times so we can add hours and minutes
    slist = start.split(':')
    # cant import re as per instructions
    # split the first list again
    a = slist[1]
    a = a.split()
    # now we have 2 lists with relevant data
    first = [slist[0], a[0], a[1]]
    second = duration.split(':')
    # math
    hours = int(first[0]) + int(second[0])
    minutes = int(first[1]) + int(second[1])
    meridien = first[2].lower()
    # other variables
    daycount = 0
    days = ''
    day = day.lower()
    # minutes to hours
    if minutes >= 60:
        minutes = minutes - 60
        hours = hours + 1
    # scaling hours with more time added
    while hours > 12:
        if hours > 12 and meridien.lower() == 'pm':
            meridien = 'AM'
            hours = hours - 12
            daycount = daycount + 1

        elif hours > 12 and meridien.lower() == 'am':
            meridien = 'PM'
            hours = hours - 12
    # for when hours equil 12
    if hours == 12 and meridien.lower() == 'pm':
        meridien = 'AM'
        daycount = daycount + 1

    elif hours == 12 and meridien.lower() == 'am':
        meridien = 'PM'

    # used to iterate through the list and find the correct day (x days later)
    dlist = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day in dlist:
        d = dlist.index(day.lower())
        dcount = daycount
        while dcount > 0:
            if d >= 6:
                d = d - 7
            d = d+1
            dcount = dcount - 1
        print(d)

    # formatting.. lots of if else statements because of optional day argument
    # messing with line spacing

    if daycount == 0 and day != '':
        new_time = (str(hours) + ':' + str(minutes).zfill(2) +
                    " " + meridien.upper() + ', ' + day.capitalize())
    elif daycount == 0 and day == '':
        new_time = (str(hours) + ':' + str(minutes).zfill(2) +
                    " " + meridien.upper())
    elif daycount == 1 and day != '':
        new_time = (str(hours) + ':' + str(minutes).zfill(2) + " " +
                    meridien.upper() + ', ' + dlist[d].capitalize() + ' (next day)')
    elif daycount == 1 and day == '':
        new_time = (str(hours) + ':' + str(minutes).zfill(2) +
                    " " + meridien.upper() + ' (next day)')
    elif daycount > 1 and day != '':
        new_time = (str(hours) + ':' + str(minutes).zfill(2) + " " +
                    meridien.upper() + ', ' + dlist[d].capitalize() + " (" + str(daycount) + ' days later)')
    elif daycount > 1 and day == '':
        new_time = (str(hours) + ':' + str(minutes).zfill(2) + " " +
                    meridien.upper() + " (" + str(daycount) + ' days later)')

    return new_time.rstrip()
