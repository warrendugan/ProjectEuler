# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def main(max):
    result = sumMultiples(max, 3)
    result += sumMultiples(max, 5)
    result -= sumMultiples(max, 15)
    return result

def sumMultiples(max, multiple):
    if max % multiple == 0:
        max = (max / multiple) -1
    else:
        max /= multiple
    sum = 0
    start = 0
    while start <= max:
        sum += start
        start += 1
    return multiple * sum

print main(1000)
# 233168
# [Finished in 0.028s]
