# Find Non-repeating characters of a String
a=input("Enter the String: ")
l=[]
for i in a:
    if a.count(i)==1:
        l.append(i)
print(l)


# Example 1:
# Input: string = “google”
# Output: l,e

# Explanation: Non repeating characters are l,e.

# Example 2:
# Input: string = “yahoo”
# Output: y,a,h
# Explanation: Non repeating characters are y,a,h