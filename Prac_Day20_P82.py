# Check if two Strings are anagrams of each other
a = input("Enter the first string: ")
b = input("Enter the second string: ")
if sorted(a)==sorted(b):
    print("Anagram")
else:
    print("Not Anagram")



# Example 1:
# Input: CAT, ACT
# Output: true
# Explanation: Since the count of every letter of both strings are equal.

# Example 2:
# Input: RULES, LESRT 
# Output: false
# Explanation: Since the count of U and T  is not equal in both strings.