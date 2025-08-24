#Day9 P44
#Find LCM of two numbers
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
l=[]
l1=[]
for i in range(1,10+1):
    m=a*i
    l.append(m)
for j in range(1,10+1):
    m1=b*j
    l1.append(m1)
c=list(set(l) & set(l1))
print(min(c))