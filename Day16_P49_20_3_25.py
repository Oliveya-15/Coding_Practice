# Check if the given number is Harshad(Or Niven) Number
n=int(input("Enter the number: "))
m=n
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
if m%s == 0:
    print("Harshad(Or Niven) Number")
else:
    print("Not a Harshad(Or Niven) Number")


# Example 1:
# Input: 378
# Output: Yes it is a Harshad number.
# Explanation: 3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number.

# Example 2:
# Input: 379
# Output: No
#  it is not a Harshad number.
# Explanation: 3+7+9=19. 379 is not divisible by 19. Therefore 379 is not a harshad number.