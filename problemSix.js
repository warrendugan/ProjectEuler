const sumSquares = n => (n*(n+1)*((2*n) + 1)) / 6
const squareSums = n => ((n*(n+1)) / 2) * ((n*(n+1)) / 2)
console.log(squareSums(100) - sumSquares(100))
