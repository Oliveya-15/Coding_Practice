a = list(map(int,input("Enter the element: ").split()))
b = list(map(int,input("Enter the element: ").split()))
l=[]
l1=[]
l2=[]
for i in b:
    if i not in a:
        l.append(i)
for j in a:
    if j not in b:
        l1.append(j)
for k in a+b:
    if k not in l2:
        l2.append(k)
print(l)
print(l1)
print(l2)