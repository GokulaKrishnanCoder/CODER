n=int(input("Enter number of elements in a list"))
a=list()
for i in range(0,n):
    b=int(input("Enter the elements of the list"))
    a.append(b)
c=int(input("Enter the element to be found"))
d=len(a)-a.index(c)
print("positive index position of the search element:",a.index(c))
print("Negative index position of the search element:-",d)
