# Sum of the Numbers in a String
a = input("Enter the String: ")
s=0
l=["1","2","3","4","5","6","7","8","9"]
for i in a:
    if i in l:
        s=s+int(i)
print(s)


# Example :
# Input: string = “1xyz23”
# Output: 24