#Check if a number is Armstrong Number or not
n=int(input("Enter the Number: "))
m=n
s=0
while n>0:
    r=n%10
    s=s+(r*r*r)
    n=n//10
if m==s:
    print("The Number is ArmStrong",m)
else:
    print("The Number is Not a ArmStrong number: ",m)


#Input: n = 153
#Output: 153 is a Armstrong Number