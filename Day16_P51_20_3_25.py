# Sum Of Digits of A Number
n = int(input("Enter the number: "))
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print(s)

# Example 1:
# Input: N = 472
# Output: 13
# Explanation: The digits in the number are 4,7 and 2. Summing them up gives us a value of 13

# Example 2:
# Input: N = 102
# Output: 3
# Explanation: The digits in the number are 0, 1, and 2. Summing them up gives us a value of 3