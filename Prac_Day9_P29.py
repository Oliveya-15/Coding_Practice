# Check if a number is perfect or not
n = int(input("Enter the number: "))
p=0
for i in range(1,n):
    if n%i==0:
        p=p+i
if p==n:
    print("No is perfect")
else:
    print("No is not perfect")