n = list(map(int,input("Enter the elements:").split()))
l=[]
for i in n:
    if i not in l:
        l.append(i)
l.sort()
print(l)