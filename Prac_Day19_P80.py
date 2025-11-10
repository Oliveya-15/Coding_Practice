# Calculate Frequency of characters in a String
a = input("Enter the string: ")
l={}
for i,val in enumerate (a):
    b=a.count(val)
    if b>1:
        l[val]=b
print(l)

