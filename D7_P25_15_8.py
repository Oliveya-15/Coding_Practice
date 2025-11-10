#Day7 P25
#Check if a number is Armstrong or Not
n=int(input("Enter the number: "))
s,m=0,n
while n>0:
    r=n%10
    s=s+(r*r*r)
    n=n//10
if m==s:
    print("Armstrong")
else:
    print("Not Armstrong")