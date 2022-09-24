# Project Euler Solution 48
# Circa September 2022
# A program by Tyler Serio
# Python 3.9.6

# The Problem:
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

# There is a less resource wasteful solution.
# This is not that solution.
# Simple solution:
x = 1
y = 0
z = 0
a = 0
answer = []
print("Running!")
while x < 1001:
    y = x ** x
    z += y
    x += 1
z = list(str(z))
z.reverse()
while a < 10:
    answer.append(z[a])
    a += 1
answer.reverse()
answer = "".join(answer)
print("Answer: " + answer)
