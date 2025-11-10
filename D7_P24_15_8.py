#Day7 P24
#Find all Prime Numbers in a given range
n=int(input("Enter Starting range: "))
m=int(input("Enter Ending range: "))
l=[]
for i in range(n,m+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        l.append(i)
print(l)

