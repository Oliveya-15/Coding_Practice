# Check if a number is prime or not
n = int(input("Enter the number: "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("No is Prime")
else:
    print("No is not Prime")
