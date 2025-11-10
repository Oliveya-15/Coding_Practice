# Bubble Sort Algorithm
a = list(map(int,input("Enter the values: ").split()))
n=len(a)
for i in range(n-1):
    ptr=0
    while(ptr<n-1):
        if(a[ptr]>a[ptr+1]):
            t=a[ptr]
            a[ptr]=a[ptr+1]
            a[ptr+1]=t
        ptr+=1
print(a)