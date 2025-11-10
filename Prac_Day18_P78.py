# Sum of the Numbers in a String
a = input("Enter the string: ")
l=["0","1","2","3","4","5","6","8","9"]
s=0
for i in a:
    if i in l:
        s=s+int(i)
print(s)