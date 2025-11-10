# Insertion Sort algorithm
n=int(input("Enter the range: "))
a = list(map(int,input("Enter the Values: ").split()))
for i in range(1,n):
    temp=a[i]
    j=i-1
    while((a[j]>temp) and (j>=0)):
        a[j+1]=a[j]
        j-=1
    a[j+1]=temp
print(a)

