# Subsets of a given list
n = list(map(int,input("Enter the elements: ").split()))
t=pow(2,len(n))
for i in range(t):
    l=[]
    for j in range(len(n)):
        if (i >> j) & 1:
            l.append(n[j])
    print(l)