#Remove duplicate from a sorted array
n=int(input("Enter the range: "))
a=list(map(int,input("Enter the numbers: ").split()))
f=[]
a.sort()
for i in a:
    if i not in f:
        f.append(i)
print("The new array is: ",f)
        
 