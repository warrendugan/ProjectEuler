# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99. 
# Find the largest palindrome made from the product of two 3-digit numbers.
# 906609
# [Finished in 0.368s]

def isPalindrome(number):
    string = str(number)
    length = len(string)
    i = 0
    while(i < (length / 2)):
        if(string[i] != string[length -1 - i]): return False
        i += 1
    return True

def createNumbers():
    MAX = 0
    a = 999
    while(a > 99):
        b = a
        while(b > 99):
            result = a * b
            if(isPalindrome(result) and result > MAX):
                MAX = result
            b -= 1
        a -= 1
    return MAX

print createNumbers()
