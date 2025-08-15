#Day7 P19
#Search an Element in an Array 
a=list(map(int,input("Enter the values: ").split()))
k=int(input("Enter the searching value: "))
c=0
for i in a:
    if i==k:
        print(a.index(i))
        c=c+1
if c<=0:
    print("Value not found")