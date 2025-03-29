# Remove brackets from an algebraic expression
a = input("Enter the Expression: ")
s=[]
a=list(a)
for i in a:
    if i!="(" and i!=")":
        s.append(i)
print("".join(s))

"""
Why we are using and instead of or ?

if we use =>  if i != "(" or i != ")":
it always return True, which is why it does not remove ( or ).

"""
# Example 1:
# Input: “a+((b-c)+d)”
# Output: “a+b-c+d”
# Explanation: Removed all the brackets in the algebric expression.

# Example 2:
# Input: “(((a-b))+c)”
# Output: “a-b+c”
# Explanation: Removed all the brackets in the algebric expression.