# Project Euler Solution 16
# Circa September 2022
# A program by Tyler Serio
# Python 3.9.6

# The Problem:
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?

x = 2 ** 1000
xlist = list(map(int, str(x)))
answer = 0
for num in xlist:
    answer += num
print(answer)
    
