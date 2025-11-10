#Day9 P43
#Find GCD of two numbers
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
l=[]
l1=[]
for i in range(1,a+1):
    if a%i==0:
        l.append(i)
for j in range(1,b+1):
    if b%j==0:
        l1.append(j)
c=list(set(l)&set(l1))
print(max(c))