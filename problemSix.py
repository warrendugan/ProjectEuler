
def sumSquares(n):
    return (n*(n+1)*((2*n) + 1)) / 6

def squareSums(n):
    return ((n*(n+1)) / 2) * ((n*(n+1)) / 2)

def getAnswer(n):
    return squareSums(n) - sumSquares(n)

print getAnswer(100)
