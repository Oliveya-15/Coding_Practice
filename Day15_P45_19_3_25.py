# Check if a number is a Strong Number or not
n = int(input("Enter the number: "))
m=n
s=0
while n>0:
    r=n%10
    f=1
    for i in range(1,r+1):
        f=f*i
    s=s+f
    n=n//10
if s==m:
    print("Strong")
else:
    print("Try you will be Strong")


# Input: N = 145
# Output: Yes
# Explanation: 1! + 4! + 5! = 145. Hence 145 is a strong number. 
