# Project Euler Solution 6
# A program by Tyler Serio
# Circa September 2022
# Python 3.9.6

# The Problem:
# The sum of the squares of the first ten natural numbers is,
# 1 ** 2 + 2 ** 2 + ... + 10 ** 2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10) ** 2 = 55 ** 2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

x = 0
y = 0
count = 1
while count < 101:
    x += count ** 2
    y += count
    count += 1
y = y ** 2
z = y - x
answer = z
print(answer)
