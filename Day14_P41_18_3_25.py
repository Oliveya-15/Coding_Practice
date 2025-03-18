# Factorial of a number
n=int(input("Enter the range: "))
f=1
for i in range(1,n+1):
    f=f*i
print(f)

"""
range should be (1,n+1) else, if we start from 0 then in 1st iteration it will stop as 0*1=0

"""

# Input: X = 5
# Output: 120
# Explanation: 5! = 5*4*3*2*1
