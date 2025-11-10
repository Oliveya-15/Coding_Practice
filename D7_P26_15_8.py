#Day7 P26
#Check if a number is Perfect or Not
n=int(input("Enter the number: "))
p=0
for i in range(1,n):
    if n%i==0:
        p=p+i
if p==n:
    print("Perfect")
else:
    print("Not Perfect")
