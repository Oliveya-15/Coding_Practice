# Change case of each character in a string
a = input("Enter the string:")
r = ""
for i in a:
    if i.isupper():
        r += i.lower()   # r = r + i.lower()
    elif i.islower():
        r += i.upper()
    else:
        print("Something went wrong")
print(r)

# Input: String str = “javA”
# Output: JAVa
# Explanation:
#  Changed the lower case characters to uppercase and vice versa.

# Example 2:
# Input: String str = “take u forward IS Awesome”
# Output: TAKE U FORWARD is aWESOME
# Explanation: Changed the lower case characters to uppercase and vice versa.