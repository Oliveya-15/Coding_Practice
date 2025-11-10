# Capitalize first and last character of each word of a string
a = input("Enter the String: ")
l1=[]
b=a.split()
for i in b:
    f=i[0].upper()
    m=i[1:-1]
    l=i[-1].upper()
    l1.append(f+m+l)
print(" ".join(l1))