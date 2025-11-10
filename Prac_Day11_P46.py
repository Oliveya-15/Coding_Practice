# Check if a number is Automorphic Number
n = int(input("Enter the number: "))
s=n*n
s1=str(s)
n1=str(n)
l=len(n1)
if l==2:
    c=s1[-2:]
elif l==3:
    c=s1[-3:]
if c==n1:
    print("Automorphic")
else:
    print("Not Automorphic")