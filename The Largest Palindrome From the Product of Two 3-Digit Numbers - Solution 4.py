# Project Euler Solution 4
# Circa August 2022
# A program by Tyler Serio
# Python 3.9.6

# The Problem:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

limit = 999 * 999
while limit > 10000:
    limit -= 1
    limitnum = list(map(int, str(limit)))
    rlimitnum = list(map(int, str(limit)))
    rlimitnum.reverse()
    if limitnum == rlimitnum:
        sublimit = 999
        while sublimit > 100:
            if limit % sublimit == 0:
                x = sublimit
                y = int(limit / sublimit)
                yl = list(map(int, str(y)))
                if len(yl) == 3:
                    answer = str(x) + " X " + str(y) + " = " + str(limit)
                    limit = 0
                else:
                    break
            else:
                sublimit -= 1
print(answer)
