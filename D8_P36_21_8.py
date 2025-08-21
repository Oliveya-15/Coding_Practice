#Day8 P36
#Maximum and Minimum Digit in a Number
n=int(input("Enter the number: "))
l=0
s=9
while n>0:
    r=n%10
    l=max(l,r)
    s=min(s,r)
    n=n//10
print("Largest",l)
print("Smallest",s)


"""
Input: N = 2746
Output: Largest digit: 7
        Smallest digit: 2
Explanation: By simply going through the digits of 
the number, we figure out the largest and smallest 
digit in the number.
"""