#Check if a number is Palindrome or Not
n=int(input("Enter the number: "))
m=n
p=0
while n>0:
    r=n%10
    p=(p*10)+r
    n=n//10
if m==p:
    print("Palindrome Number")
else:
    print("Not a palindrome number")




"""
n=121
r=1
p=(0*10)+1 = 1
n=12

n=12
r=2
p=(1*10)+2 = 12
n=1

n=1
r=1
p=(12*10)+1 = 121
n=0

if m==p
  m=121 == p=121 => Palindrome

"""

# input: 121
# output: Palindrome