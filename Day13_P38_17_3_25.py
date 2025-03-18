# Reverse digits of a number
n = int(input("Enter the number: "))
while n>0:
    r=n%10
    print(r, end="")
    n=n//10
    

# Input: N = 472
# Output: 274
# Explanation: Reading the number from back to front, we see that the output should be 274
