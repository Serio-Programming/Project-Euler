# Euler Project Solution 7
# Circa August 2022
# A program by Tyler Serio
# Python 3.9.6

# The Problem:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

prime = 13
pcount = 6
while pcount < 10001:
    prime+= 1
    dividing = prime
    while dividing > 0:
        dividing -= 1
        remainder = prime % dividing
        if dividing == 1:
            pcount += 1
        if remainder == 0:
            dividing = 0
            break
answer = prime
print(answer)
            
