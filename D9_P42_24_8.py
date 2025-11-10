#Day9 P42
#Check a number is Automorphic number or not
n=int(input("Enter the number: "))
s=n*n
d=list(str(s))
l=len(str(n))
e=d[-l:]
m=int("".join(e))
if m==n:
    print("Automorphic")
else:
    print("Not Automorphic")