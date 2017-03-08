const problemOne = max => {
  let sum = 0
  sum += sumMultiples(max, 3)
  sum += sumMultiples(max, 5)
  sum -= sumMultiples(max, 15)
  return sum
}

const sumMultiples = (max, multiple) => {
  max = Math.ceil(max/multiple - 1)
  let sum = 0, start = 0
  while(start <= max) {
    sum += start
    start++
  }
  return multiple * sum
}

const result = problemOne(1000)
console.log(result)
// 0.147s
