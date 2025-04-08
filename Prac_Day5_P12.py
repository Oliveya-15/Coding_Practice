n = int(input("Enter the range: "))
a = list(map(int,input("Enter the values: ").split()))
f=[]
for i in a:
    if a.count(i) == 1:
        f.append(i)
print(f)