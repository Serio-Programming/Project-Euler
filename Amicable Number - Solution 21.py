# Project Euler Solution 21
# Circa October 2022
# A program by Tyler Serio
# Python 3.9.6

# The Problem:
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

number = 1
place = 0
div_check = 2
am_nums = []
even_divisors = []
more_even_divisors = []
print("Running!")
while number < 10000:
    if number in am_nums:
        number += 1
    place = number
    even_divisors.append(1)
    while div_check < place:
        if number % div_check == 0:
            even_divisors.append(div_check)
            even_divisors.append(int(number / div_check))
            place = int(number / div_check)
        div_check += 1
    div_check = 2
    t = "gs"
    more_even_divisors.append(1)
    place = sum(even_divisors)
    while div_check < place:
        if sum(even_divisors) % div_check == 0:
            more_even_divisors.append(div_check)
        div_check += 1
    if sum(more_even_divisors) == number and sum(even_divisors) != number:
        am_nums.append(place)
        am_nums.append(sum(more_even_divisors))
        print(am_nums)
    div_check = 2
    even_divisors.clear()
    more_even_divisors.clear()
    number += 1
print("The answer is : " + str(sum(am_nums)))
            
