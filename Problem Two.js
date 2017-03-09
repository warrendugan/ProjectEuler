// returns the fibonacci number of a given value
const getFib = value => {
  return (Math.pow(Phi, value) - Math.pow(-phi, value)) / Math.sqrt(5)
}

const getEvenFib = value => {
  let start = 0, sum = 0
  while(start < value) {
    var fib = getFib(start)
    start++
    if(fib % 2 === 0) {
      if(fib < 4000000) {
        sum += fib
      } else {
        console.log('Over 4mil')
        return fib
      }
    }
  }
}

const Phi = (Math.sqrt(5) + 1) / 2
const phi = Phi - 1

const result = Math.round(getFib(9000))
console.log(result)
