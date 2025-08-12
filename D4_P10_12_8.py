#Day3 P8
#Remove Duplicates in-place from Sorted Array
a=list(map(int,input("Enter the values: ").split()))
l=[]
a.sort()
for i in a:
    if i not in l:
        l.append(i)
print(l)