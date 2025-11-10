# Remove all vowels from the String
a = input("Enter the character: ")
l=["a","e","i","o","u","A","E","I","O","U"]
s=[]
for i in a:
    if i not in l:
        s.append(i)
print("".join(s))
        