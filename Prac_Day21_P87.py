# Change every letter with next lexicographic alphabet
a=input("Enter the string: ")
r=""
for i in a:
    if i=='z':
        r=r+'a'
    elif i=='Z':
        r=r+'A'
    else:
        r=r+ chr(ord(i)+1)
print(r)



# Example 1:
# Input: string str = “abcdxyz”
# Output: bcdeyza
# Explanation:
# a -> b
# b -> c
# c -> d
# x -> y
# y -> z   like this