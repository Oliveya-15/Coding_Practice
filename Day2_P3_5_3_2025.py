a=list(map(int,input("enter the Numbers: ").split()))
small=a[0]
large=a[0]
for i in a:
    if i > large:
        large = i
print("The Largest Number is: ",large)
for j in a:
    if j < small:
        small = i
print("The Largest Number is: ",small)