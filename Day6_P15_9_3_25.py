# Find & print all Non-repeating elements
n=int(input("Enter the range: "))
a=list(map(int,input("Enter the numbers: ").split()))
f=[]
for i in a:
    if a.count(i)<=1:
        f.append(i)
print("The array with no repetative number is: ",f)