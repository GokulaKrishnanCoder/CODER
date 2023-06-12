def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def palindrome(n):
    return str(n) == str(n)[::-1]

def countdigits(n):
    return len(str(n))


num = int(input("Enter a number: "))

if num % 2 == 1:  
    fact = factorial(num)
    digits = countdigits(fact)
    print("The factorial of ",num," is ",fact)
    print("The number of digits in the factorial is ",digits)
else:  
    if palindrome(num):
        print(num," is a palindrome")
    else:
        print(num," is not a palindrome")
