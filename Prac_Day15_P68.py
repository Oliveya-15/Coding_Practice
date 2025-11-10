# Quick Sort Algorithm
a=list(map(int,input("Enter the values: ").split()))
if len(a)>1:
    p=a[len(a)//2]
    
    l=[]
    for i in a:
        if i<p:
            l.append(i)
    m=[]
    for i in a:
        if i==p:
            m.append(i)
    r=[]
    for i in a:
        if i>p:
            r.append(i)
    s=sorted(l)+m+sorted(r)
else:
    s=a
print(s)

