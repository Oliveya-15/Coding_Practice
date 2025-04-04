# Count frequency of element in an array
n = int(input("Enter the range: "))
a = list(map(int,input("Enter the numbers: ").split()))
l=[]
for i in range(1,n+1):
    l.append(a.count(i))
print(l)