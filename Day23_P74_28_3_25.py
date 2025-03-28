# Remove Spaces from a String
a = input("Enter the string: ")
a=list(a)
for i in a:
    if i==" ":
        a.remove(i)
print("".join(a))



# Example 1:
# Input: str = “Take you forward” 
# Output: Takeyouforward
# Explanation: After removing all the whitespaces Takeyouforward is the result

# Example 2:
# Input: str = “How are you doing”
# Output: Howareyoudoing
# Explanation: After removing all the whitespaces Howareyoudoing is the result