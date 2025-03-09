#Find and print all repeating elements
n = int(input("Enter the range: "))
a = list(map(int,input("Enter the numbers: ").split()))
f=[]
m=[]
for i in a:
    if a.count(i)>1:
        f.append(i)
for j in f:
    if j not in m:
        m.append(j)
print("The Duplicate elements are: ",m)




