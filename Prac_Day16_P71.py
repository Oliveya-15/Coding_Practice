# Count number of vowels, consonants, spaces in String
a = input("Enter the String: ")
l = ["a","e","i","o","u"]
v,c,s=0,0,0
for i in a:
    if i in l:
        v+=1
    elif i==" ":
        s+=1
    else:
        c+=1
print("Vowels: ",v)
print("Consonants: ",c)
print("Spaces: ",s)
