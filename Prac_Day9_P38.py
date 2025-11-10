# Reverse digits of a number
n = int(input("Enter the number: "))
while n>0:
    r = n%10
    print(r,end="")
    n = n//10
