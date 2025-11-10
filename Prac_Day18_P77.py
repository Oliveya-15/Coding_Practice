# Remove brackets from an algebraic expression
a = input("Enter the expression: ")
s=[]
for i in a:
    if i != ")" and i != "(":
        s.append(i)
print("".join(s))

# Input: “ a+((b-c)+d) ”
# Output: “ a+b-c+d ”