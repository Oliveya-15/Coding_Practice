# rearrange array in increasing or decreasing order
n = int(input("Enter the range: "))
a = list(map(int,input("Enter the numbers: ").split()))
for i in range(n):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print("Increasing order: ",a)
for i in range(n):
    for j in range(n-i-1):
        if a[j] < a[j+1]:
            a[j], a[j + 1] = a[j + 1], a[j]  
print("Decreasing order: ",a)

"""
a.sort()
print(a)         
a.reverse()
print(a)



temp=a[j]          a[j] = a[j+1]     this 2 part of code we can write it like this in one line : a[j],a[j+1] = a[j+1],a[j]
a[j]=a[j+1]        a[j+1] = a[j]
a[j+1]=temp

"""
