# Project Euler Solution 14
# Circa September 2022
# A program by Tyler Serio
# Python 3.9.6

# The Problem:
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

x = 999999
tcount = 0
answer = [x, tcount]
print("Running!")
while x > 1:
    y = x
    while y > 1:
        if y % 2 == 0:
            y = int(y / 2)
            tcount += 1
        else:
            y = (3 * y) + 1
            tcount += 1
        if answer[1] < tcount:
            answer[0] = x
            answer[1] = tcount
    x -= 1
    tcount = 0
print("The answer: ")
print(answer)
