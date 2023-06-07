#Triangle posssibility
a=int(input("Enter the legth of first side"))
b=int(input("Enter the legth of second side"))
c=int(input("Enter the legth of third side"))
if(a+b>c and b+c>a and a+c>b):
    print("Triangle is possible")
else:
    print("Triangle is not possible")
            
