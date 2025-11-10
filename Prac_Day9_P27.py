# Find prime numbers in a given range
n = int(input("enter the starting position of the range: "))
m = int(input("enter the ending position of the range: "))
f=[]
for i in range(n,m+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        f.append(i)
print(f)
