def recursive(n):
   if(n<=1):
      return n
   else:
      return(recursive(n-1)+recursive(n-2))
   
n=int(input("Enter a number to find fibonacci series"))
for i in range(n):
      print(recursive(i))
