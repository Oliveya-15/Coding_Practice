# Find LCM of two numbers
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
l=a*b
f=[]
f1=[]
f2=[]
for i in range(1,a+1):
    if a%i==0:
        f.append(i)
for j in range(1,b+1):
    if b%j==0:
        f1.append(j)
for m,val in enumerate(f):
    for n,value in enumerate(f1):
        if val==value:
            f2.append(i)
gcd=max(f2)
lcm=l/gcd
print(lcm)


# LCM(a,b) = a*b / GCD(a,b)