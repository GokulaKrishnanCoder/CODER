#code for finding the n'th power is even of odd
def power(b,n):
    if (b**n%2==0):
        return 0
    else:
        return 1
b=int(input("Enter the base number:"))
n=int(input("Enter the power value:"))
if power(b,n)==0:
   print(b,"power",n,"is even")
else:
    print(b,"power",n,"is odd")
