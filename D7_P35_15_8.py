#Day7 P35
#Reverse Digit of number
n=int(input("Enter the number: "))
while n>0:
    r=n%10
    print(r)
    n=n//10