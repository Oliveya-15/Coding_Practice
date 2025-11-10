#Print all Prime Factors of the given number
n = int(input("Enter the range: "))
s=[]
s1=[]
for i in range(1,n+1):
    if n%i==0:
        s.append(i)
for k in s:
    c=0
    for j in range(1,k+1):
        if k%j==0:
            c+=1
    if c==2:
        s1.append(k)
print(s1)