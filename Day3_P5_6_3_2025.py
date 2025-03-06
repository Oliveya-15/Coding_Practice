#Count Frequency of each element in an array
n=int(input("Enter the range: "))
a = list(map(int,input("Enter the Numbers: ").split()))
f={}
for i in a:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)

