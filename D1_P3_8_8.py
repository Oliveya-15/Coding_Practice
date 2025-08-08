#Day1 P3
#Reverse of an array

a=list(map(int,input("Enter the numbers: ").split()))

r=[]
for i in range(len(a)-1,-1,-1):
    r.append(a[i])
print(r)