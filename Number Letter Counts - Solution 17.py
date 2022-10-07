# Project Euler Solution 17
# Circa October 2022
# A program by Tyler Serio
# Python 3.9.6

# The Problem:
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

dictionary = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
              11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
              19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}
print("Running!")
n = 1
count = 0
while n < 1001:
    if n < 21:
        print(dictionary[n])
        count += len(dictionary[n])
    elif 20 < n < 100:
        if n % 10 == 0:
            print(dictionary[n])
            count += len(dictionary[n])
        else:
            x = list(str(n))
            print(str(dictionary[10 * int(n / 10)]) + " " + dictionary[int(x[1])])
            count += len(str(dictionary[10 * int(n / 10)] + " " + dictionary[int(x[1])]).replace(" ", ""))
    elif 1000 > n > 99:
        x = list(str(n))
        if int(x[1] + x[2]) == 0:
            print(str(dictionary[int(x[0])]) + " hundred")
            count += len(str(dictionary[int(x[0])] + " hundred").replace(" ", ""))
        elif int(x[1] + x[2]) > 20:
            t = "gs"
            print(str(dictionary[int(x[0])]) + " hundred and " + dictionary[int(x[1]) * 10] + " " + dictionary[int(x[2])])
            count += len(str(dictionary[int(x[0])] + " hundred and " + dictionary[int(x[1]) * 10] + " " + dictionary[int(x[2])]).replace(" ", ""))
        else:
            print(str(dictionary[int(x[0])]) + " hundred and " + dictionary[int(x[1] + x[2])])
            count += len(str(dictionary[int(x[0])] + " hundred and " + dictionary[int(x[1] + x[2])].replace(" ", "")).replace(" ", ""))
    elif n > 999:
        print("one thousand")
        count += len("one thousand".replace(" ", ""))
    else:
        print(n)
        print("Derp")
    n += 1
print("The answer is : " + str(count))
        
