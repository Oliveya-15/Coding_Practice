# Change case of each character in a string
a = input("Enter the String: ")
r=""
for i in a:
    if i.isupper():
        r=r+i.lower()
    elif i.islower():
        r=r+i.upper()
    else:
        print("Problem")
print(r)