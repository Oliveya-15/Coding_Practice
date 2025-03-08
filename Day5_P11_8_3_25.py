#Remove Duplicate element from a unsorted array
n=int(input("Enter the range: "))
a=list(map(int,input("Enter the numbers: ").split()))
f=[]
for i in a:
    if i not in f:
        f.append(i)
print("The new array is: ",f)