#Day7 P23
#Check if a number is Prime or Not
n=int(input("enter the value: "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
if c==2:
    print("The number is Prime")
else:
    print("The number is not Prime")