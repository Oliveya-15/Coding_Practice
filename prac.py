"""n=int(input("Enter the value: "))
a,b=0,1
print(a,b,end=" ")
for i in range(2,n+1):
    c=a+b
    print(c,end=" ")
    a,b=b,c"""
l=list(map(int,input("Enter the values: ").split()))
print(l)