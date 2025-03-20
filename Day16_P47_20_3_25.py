#Find GCD of two numbers
n1 = int(input("Enter the 1st no: "))
n2 = int(input("Enter the 2nd no: "))
l=[]
m=[]
s=[]
for i in range(1,n1+1):
    if n1%i == 0:
        l.append(i)
for i in range(1,n2+1):
    if n2%i==0:
        m.append(i)
for i, val in enumerate(l):
    for j,value in enumerate(m):
        if val == value:
            s.append(val)
print(max(s))

"""
GCD formula :- GCD(a,b)=GCD(b,amodb)

while n2:
    n1,n2 = n2, n1%n2
print(n1)



n1 = 9, n2 = 12
Step 1:
Compute n1 % n2 → 9 % 12 = 9
Swap: n1 = 12, n2 = 9
Step 2:
Compute n1 % n2 → 12 % 9 = 3
Swap: n1 = 9, n2 = 3
Step 3:
Compute n1 % n2 → 9 % 3 = 0
Swap: n1 = 3, n2 = 0
End Condition:
Since n2 = 0, the GCD is 3.
"""


# Input:N1 = 9, N2 = 12
                
# Output:3
# Explanation:Factors of 9: 1, 3 and 9
# Factors of 12: 1, 2, 3, 4, 6, 12
# Common Factors: 1, 3 out of which 3 is the greatest hence it is the GCD.