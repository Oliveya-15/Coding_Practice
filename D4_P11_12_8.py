#Day4 P11
#Remove Duplicate element from a unsorted array
a=list(map(int,input("Enter the values: ").split()))
l=[]
for i in a:
    if i not in l:
        l.append(i)
print(l)