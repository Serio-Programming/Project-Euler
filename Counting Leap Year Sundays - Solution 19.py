# Project Euler Solution 19
# Circa September 2022
# A program by Tyler Serio
# Python 3.9.6

# The Problem:
# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
year = 1900
leapyear = False
leapcount = 0
month = months[0]
dcount = 0
totaldcount = 0
dayiter = iter(days)
monthiter = iter(months)
s1count = 0
while year < 2001:
    dcount += 1 
    wday = next(dayiter)
    if month == "January" and dcount == 1:
        year += 1
        if leapyear == False:
            leapcount += 1
        if leapyear == True:
            leapcount = 0
    if dcount == 28 and month == "February" and leapyear != True:
        month = next(monthiter)
        totaldcount += dcount
        dcount = 0
    if dcount == 29 and month == "February" and leapyear == True:
        month = next(monthiter)
        totaldcount += dcount
        dcount = 0
    if dcount == 30 and (month == "September" or month == "April" or month == "June" or month == "November"):
        month = next(monthiter)
        totaldcount += dcount
        dcount = 0
    if dcount == 31 and (month == "January" or "July" or "December" or "March" or "August" or "May" or "October"):
        month = next(monthiter)
        totaldcount += dcount
        dcount = 0
    if wday == "Sunday" and dcount == 1:
        s1count += 1
    if wday == "Sunday":
        dayiter = iter(days)
    if month == "December":
        monthiter = iter(months)
    if leapcount == 4:
        leapyear == True
answer = s1count
print(answer)
