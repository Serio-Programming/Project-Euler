# Project Euler Solution 1
# Circa August 2022
# A program by Tyler Serio
# Python 3.9.6

# The Problem:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

x = 1
s = 0
while x < 1000:
    if x % 3 == 0 or x % 5 == 0:
        s += x
    x += 1
answer = s
print(answer)
