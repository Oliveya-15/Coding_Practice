# Check if the given String is Palindrome or not
a = input("Enter the string: ")
r = "".join(reversed(a))
print(r)
if a==r:
    print("Pelindrome")
else:
    print("Not Pelindrome")


