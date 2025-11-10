# Find Non-repeating characters of a String
a = input("Enter the string: ")
l=[]
for i in a:
    if a.count(i)==1:
        l.append(i)
print(l)