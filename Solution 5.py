# Project Euler Solution 5
# A program by Tyler Serio
# Circa September 2022
# Python 3.9.6

# The Problem: 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

answer = 0
x = 2520
while answer == 0:
    x += 2520
    counting = 20
    while counting > 0:
        if x % counting != 0:
            counting = 0
        if counting == 1:
            answer = x
        counting -= 1
print(answer)
