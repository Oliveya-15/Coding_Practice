# Print all repeating elements in an array
a = list(map(int,input("Enter the values: ").split()))
f=[]
for i in a:
    if a.count(i) > 1:
        if i not in f:
            f.append(i)
print(f)