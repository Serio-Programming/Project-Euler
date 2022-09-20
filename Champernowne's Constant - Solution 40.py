# Project Euler Solution 40
# Circa September 2022
# A program by Tyler Serio
# Python 3.9.6

# The Problem:
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

print("Running!")
steps = [1, 10, 100, 1000, 10000, 100000, 1000000]
constant = []
d = []
iteration = 1
removed = 1
while iteration < 1000001:
    ilist = list(str(iteration))
    for n in ilist:
        constant.append(n)
    if iteration == steps[0]:
        d.append(constant[iteration - removed])
        removed += len(constant)
        constant.clear()
        del steps[0]
    iteration += 1

answer = 1
for n in d:
    answer *= int(n)
print(answer)
