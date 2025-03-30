# Check if two Strings are anagrams of each other
a=input("enter the string: ")
b=input("Enter the String: ")
if sorted(a) == sorted(b):
    print("True")
else:
    print("False")





# Example 1:
# Input: CAT, ACT
# Output: true
# Explanation: Since the count of every letter of both strings are equal.

# Example 2:
# Input: RULES, LESRT 
# Output: false
# Explanation: Since the count of U and T  is not equal in both strings.