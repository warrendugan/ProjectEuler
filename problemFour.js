const isPalindrome = number => number.toString() === number.toString().split('').reverse().join('')

const getLargestPalidrome = () => {
    MAX = 0
    let a = 999
    while (a > 99) {
        let b = a
        while (b > 99) {
            result = a * b
            if (isPalindrome(result) && result > MAX) MAX = result
            b--
        }
        a--
    }
    return MAX
}

console.log(getLargestPalidrome())
