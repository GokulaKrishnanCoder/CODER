#code for finding factorial of a number
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter a number to find factorial:"))
print("The factorial of the given number is :", fact(n))
