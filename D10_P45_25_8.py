#Day10 P45
#Check a number is Harshed number or not
n=int(input("Enter the number: "))
s,m=0,n
while n>0:
    r=n%10
    s=s+r
    n=n//10
if m%s==0:
    print("Harshed Number")
else:
    print("Not a Harshed Number")



"""
Example 1:
Input: 378
Output: Yes it is a Harshad number.
Explanation: 3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number.
"""