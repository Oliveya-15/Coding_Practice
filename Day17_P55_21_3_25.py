# Replace all the 0’s with 1 in a given integer
n=int(input("Enter the number: "))
s=str(n).replace("0","1")
print(s)


# Example 1:
# Input: N = 102003
# Output: 112113
# Explanation: The 2nd,4th and 5th position from left contain 0.The resultant integer has replaced the 0’s in those  positions with 1.

# Example 2:
# Input:  204
# Output: 214
# Explanation: The 2nd position from left contain 0. The resultant integer has replaced the 0 in that position with 1.