# Print all pelindrome number in given range
n = int(input("Enter starting of the range: "))
m = int(input("Enter ending of the range: "))
f=[]
for i in range(n,m+1):
    s=0
    p=i
    while i>0:
        r = i%10
        s = (s*10)+r
        i = i//10
    if s==p:
        f.append(p)
print(f)