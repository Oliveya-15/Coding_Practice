# Remove Spaces from a String
a = input("Enter the sentence: ")
a = list(a)
for i in a:
    if i==" ":
        a.remove(i)
print("".join(a))


"""
s = []
for i in a:
    s.append(i)
for j in s:
    if j==" ":
        s.remove(j)
print("".join(s))"""
