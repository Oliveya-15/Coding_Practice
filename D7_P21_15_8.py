#Day7 P21
#Check if a number is Palindrome or Not
n=int(input("Enter the number: "))
p,m=0,n
while n>0:
    r=n%10
    p=(p*10)+r
    n=n//10
if m==p:
    print("Pelindrome")
else:
    print("Not Pelindrome")
