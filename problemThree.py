# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# result 6857
# [Finished in 0.083s]

def isPrime(checkNumber):

    if checkNumber <= 1: return False
    if checkNumber == 2: return True
    if checkNumber == 3: return True
    if checkNumber == 5: return True

    switcher = [ 1, 7, 11, 13, 17, 19, 23, 29 ]
    if checkNumber % 30 not in switcher: return False

    a = 7
    skipCase = 1
    while(a*a <= checkNumber):

        number = checkNumber % a
        if number == 0: return False

        if skipCase == 1:
            a += 4
            skipCase = 2
        elif skipCase == 2:
            a += 2
            skipCase = 3
        elif skipCase == 3:
            a += 4
            skipCase = 4
        elif skipCase == 4:
            a += 2
            skipCase = 5
        elif skipCase == 5:
            a += 4
            skipCase = 6
        elif skipCase == 6:
            a += 6
            skipCase = 7
        elif skipCase == 7:
            a += 2
            skipCase = 8
        elif skipCase == 8:
            a += 6
            skipCase = 1

    return True

def largestPrime(number):
    if isPrime(number): return number
    limit = number
    a = 2
    while(a < limit):
        if limit % a == 0:
            limit /= a
            if isPrime(limit):
                maxFactor = limit
                break
            if isPrime(a):
                maxFactor = a
        a += 1
    return maxFactor

print largestPrime(600851475143)
