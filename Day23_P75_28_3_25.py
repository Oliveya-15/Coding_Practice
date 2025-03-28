# Remove characters from a string except alphabets
a = input("Enter the String: ")
l=["%","&","^","$","@","!","#","*"]
a=list(a)
for i in a[:]:
    if i==" " or i in l:
        a.remove(i)
print("".join(a))

"""
a[:] (a copy of a) ensures that modifying a doesn't affect the iteration.a[:] ensures safe removal without 
skipping elements. example - for i in a[:] : 
avoid skipping elements use this.
"""

# Example 1:
# Input: string str = "take12% *&u ^$#forward"
# Output: takeuforward
# Explanation:
# Characters 1,2,%,*,&,^,$,# along with whitespaces are 
# removed but the order of remaining alphabets is preserved.

# Example 2:
# Input: String str = "1.Python & 2.Java"
# Output: PythonJava
# Explanation: 
# Characters 1.&2. along with whitespaces are removed 
# but the order of remaining alphabets is preserved.