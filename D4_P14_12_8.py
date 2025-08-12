#Day4 P14
#Find all the non-repeating elements in an array
a=list(map(int,input("Enter the values: ").split()))
l=[]
for i in a:
    if a.count(i)==1:
        l.append(i)
print(l)