# Find the sum of numbers in the given range
n=int(input("Enter starting range: "))
m=int(input("Enter ending range: "))
s=0
for i in range(n,m+1):
    s=s+i
print(s)

# Example 1:
# Input: l=2, r=7
# Output: 27
# Explanation: 2+3+4+5+6+7=27. Therefore 27 is the answer.

# Example 2:
# Input: l=5, r=9
# Output: 35
# Explanation: 5+6+7+8+9=35. Therefore 35 is the answer.