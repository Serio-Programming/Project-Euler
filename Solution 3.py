# Solution 3
# Circa August 2022
# A program by Tyler Serio
# Python 3.9.6

# The Problem:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

n = 600851475143
o = n - 600851000000
while o > 0:
    if n % o == 0:
        p = int(o / 2) + 1
        while p > 0:
            if p == 1:
                answer = o
                o = 0
                break
            if o % p == 0:
                break
            p -= 1
    o -= 1
print(answer)
