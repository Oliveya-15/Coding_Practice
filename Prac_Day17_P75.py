# Remove characters from a string except alphabets
a = input("Enter the sentence: ")
l = ["%","&","^","$","@","!","#","*"," "]
s=[]
for i in a:
    if i not in l:
        s.append(i)
print("".join(s))