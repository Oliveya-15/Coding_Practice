# Print all the duplicates in the string
a = input("Enter the String: ")
l={}
for i,val in enumerate (a):
    if a.count(val)>1:
        l[val]=i
print(l)


"""l=[]
for i in a:
    if a.count(i)>1:
        l.append(i)
        True
print("".join(l))"""
