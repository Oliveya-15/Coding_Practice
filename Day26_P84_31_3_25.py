# Remove All Duplicates from a String
a = input("Enter the string: ")
d={}
s=""
for i in a:
    b=a.count(i)
    d[i]=b
for i,val in d.items():
    if val==1:
        s+=i
print(s)


# Input: s = "bcabc"
# Output: “bca"

# Explanation: Duplicate Characters are removed
# Example 2:
# Input: s = "cbacdcbc"
# Output: "cbad" 
# Explanation: Duplicate Characters are removed