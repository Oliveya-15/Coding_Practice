# Program to find Sum of GP Series
n = int(input("Enter the n value: "))
a = int(input("Enter the a value: "))
r = float(input("Enter the r value: "))
if r!=1:
    s = a*(1-pow(r,n))/(1-r)
print(s)