# Remove duplicate from a sorted array
n = int(input("Enter the range: "))
a = list(map(int,input("enter the values: ").split()))
l=[]
b = sorted(a)
for i in b:
    if b.count(i) == 1:
        l.append(i)
print(l)