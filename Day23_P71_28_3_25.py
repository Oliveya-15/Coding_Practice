# Count number of vowels, consonants, spaces in String
a = input("Enter the string: ")
l=["a","e","i","o","u","A","E","I","O","U"]
v,c,s=0,0,0
for i in a:
    if i in l:
        v+=1
    elif i==" ":
        s+=1
    else:
        c+=1
print("Consonats: ",c)
print("Vowels: ",v)
print("Spaces: ",s)


# Input: string str=”Take u forward is Awesome”
# Output: 
# Vowels: 10
# Consonants: 11
# White spaces: 4
