# Sort Elements of an Array by Frequency
a = list(map(int,input("Enter the values: ").split()))
f = []
for i in a:
    r=a.count(i)
    if i not in f:
        for _ in range(r):
            f.append(i)
f.sort()
print(f)
