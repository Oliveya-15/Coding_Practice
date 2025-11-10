# Find word with highest number of repeated letters in string
a = input("Enter the String: ")
b=a.split()
s=""
r=1
for i in b:
    h=1
    for j in i:
        c=i.count(j)
        if c>h:
            h=c
        if h>r:
            r=h
            s=i
if r==1:
    print("Not Found")
else:
    print(s)


