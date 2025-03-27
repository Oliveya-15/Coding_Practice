# Check if the given String is Palindrome or not
a=input("enter the String: ")
r="".join(reversed(a))
print(r)
if r==a:
    print("Palindrome")
else:
    print("Not Palindrome")




# Example 1:
# Input: Str =  “ABCDCBA”
# Output: Palindrome
# Explanation: String when reversed is the same as string.

# Example 2:
# Input: Str = “TAKE U FORWARD”
# Output: Not Palindrome
# Explanation: String when reversed is not the same as string.