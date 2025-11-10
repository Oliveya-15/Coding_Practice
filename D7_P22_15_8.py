#Day7 P22
#Find all Palindrome Numbers in a given range
n=int(input("Starting Range: "))
m=int(input("Ending Range: "))
l=[]
for i in range(n,m+1):
    p=0
    n1=i
    while i>0:
        r=i%10
        p=(p*10)+r
        i=i//10
    if n1==p:
        l.append(n1)
print(l)

"""
Input: min = 10 , max = 50
Output: 11 22 33 44 
Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward.
 
"""