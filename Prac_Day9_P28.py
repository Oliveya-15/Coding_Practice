# Check if a number is armstrong or not
n = int(input("Enter the number: "))
m = n
s = 0
while n>0:
    r = n%10
    s = s+(r*r*r)
    n = n//10
if s==m:
    print("No is armstrong")
else:
    print("No is not armstrong")