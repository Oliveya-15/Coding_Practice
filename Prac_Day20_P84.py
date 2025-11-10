# Remove All Duplicates from a String
a = input("Enter the String: ")
l=[]
for i in a:
    if a.count(i)==1:
        l.append(i)
print("".join(l))
        

