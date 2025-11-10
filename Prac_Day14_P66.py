# Selection Sort Algorithm
n = int(input("Enter the range: "))
a = list(map(int,input("Enter the values: ").split()))
for i in range(n-1):
    min=a[i]
    loc=i
    for j in range(i+1,n):
        if (min>a[j]):
            min=a[j]
            loc=j
    t=a[i]
    a[i]=a[loc]
    a[loc]=t
print(a)

