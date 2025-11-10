# check if a number is pelindrome or not
n = int(input("Enter the number: "))
m = n
p = 0
while n>0:
    r = n % 10
    p = (p*10)+r
    n = n // 10
if p == m:
    print("No is pelindrome")
else:
    print("Number is not pelindrome")