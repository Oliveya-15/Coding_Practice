# Remove Characters from first String present in the Second String
a=input("Enter the first string: ")
b=input("Enter the second string: ")
r=[]
r1=[]
if len(a)>len(b):
    for i in a:
        if i not in b:
            r.append(i)
    print("".join(r))
elif len(b)>len(a):
    for j in b:
        if j not in a:
            r1.append(j)
    print("".join(r1))
else:
    print("Strings are equal")           




# Example 1:
# Input: String str1 = “abcdef”
#        String str2 = “cefz”
# Output: abd
# Explanation: The common characters in both strings are c, e, f.
# So after removing these characters from string 1 we get string resulting string as abd.


# Example 2:
# Input: String str1 = “xyzpw”
#        String str2 = “lmno”
# Output: xyzpw
# Explanation: As there is no common character in both the strings, string 1 remains unchanged.