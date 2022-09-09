# Project Euler Solution 20
# Circa September 2022
# A program by Tyler Serio
# Python 3.9.6

# The Problem:
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

x = 1
n = 100
while n > 0:
    x *= n
    n -= 1
xlist = list(map(int, str(x)))
answer = 0
for num in xlist:
    answer += num
print(answer)
