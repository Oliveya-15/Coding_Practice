# Find the Position of a Substring within a String
a=input("Enter the first String: ")
b=input("Enter the second String: ")
if b in a:
    print(a.index(b))
elif a in b:
    print(b.index(a))
else:
    print("No Substring")