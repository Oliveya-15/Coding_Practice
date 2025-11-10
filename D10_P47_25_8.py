#Day10 P47
#Permutations in which N people can occupy R seats
n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))
f,f1=1,1
for i in range(1,n+1):
    f=f*i
m=(n-r)
for j in range(1,m+1):
    f1=f1*j
p=f/f1
print(p)

"""
Example 1:
Input: N = 5, r = 3
Output: 60
Explanation: To permute n people in r seats we have to find the value of n!/(n-r)!.The value of 5!/(5-3)! Is 60.

Example 2:
Input: N=6,r = 4.
Output: 360
"""