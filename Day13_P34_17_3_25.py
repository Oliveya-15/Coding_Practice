# Program to find Sum of GP Series
n = int(input("Enter the value of n: "))
a = int(input("Enter the value of a: "))
r = float(input("Enter the value of r: "))
if r!=1:
    s = a*(1-pow(r,n))/(1-r)
print(s)

# Input: a=1 , r=0.5 , n=3
# Output: 1.75
# Explanation: The sum of given GP Series is 1.75
