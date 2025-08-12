#Day4 P13
#Find all repeating elements in an array
a=list(map(int,input("Enter the values: ").split()))
l=[]
for i in a:
    if a.count(i) > 1:
        l.append(i)
print(l)