# Maximum occurring character in a string
a=input("Enter the string: ")
l={}
for i,val in enumerate(a):
    b=a.count(val)
    l[val]=b
m=max(l.values())
for i,val in l.items():
    if val==m:
        print(i)

# Example 1:
# Input: str = “takeuforward”
# Output: a
# Explanation: The character 'a' and 'r’ have the same  maximum occurrence i.e 2. Hence we can print any one of them

# Example 2:
# Input: str = “apple”
# Output: p
# Explanation: The character 'p' have the maximum occurrence i.e 2.