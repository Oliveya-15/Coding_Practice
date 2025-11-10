# Maximum occurring character in a string
a = input("Enter the string: ")
l={}
for i,val in enumerate (a):
    b=a.count(val)
    l[val]=b
m=max(l.values())
for i,val in l.items():
    if val==m:
        print(i)