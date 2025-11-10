#Day7 P31
#Find Sum of GP Series
a=int(input("Enter the value of a: "))
r=float(input("Enter the value of r: "))
n=int(input("Enter the value of n: "))
s = a*(1-pow(r,n))/(1-r) 
print(s)