# Find the Position of a Substring within a String
a = input("Enter the first string: ")
b = input("Enter the second string: ")
if a in b:
    print(b.index(a))
elif b in a:
    print(a.index(b))
else:
    print("No Match")



# Example 1:
# Input: str1 = "takeuforward"
#        str2 = “forward”
# Output: 5
# Explanation: "Forward" is present in the 5th index in "takeuforward"

# Example 2:
# Input: str1 = “hello”
#        str2 = “az”
# Output: -1
# Explanation: "az" is not a substring of "hello"