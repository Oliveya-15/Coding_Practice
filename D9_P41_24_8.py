#Day9 P41
#Check a number is Strong number or not
n=int(input("Enter the number: "))
l=[]
l1=[]
m=n
while n>0:
    r=n%10
    l.append(r)
    n=n//10
for i in l:
    f=1
    for j in range(1,i+1):
        f=f*j
    l1.append(f)
if sum(l1)==m:
    print("The number is Strong")
else:
    print("The number is not Strong")
