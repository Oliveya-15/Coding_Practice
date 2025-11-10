# Maximum and Minimum Digit in a Number
n = int(input("Enter the number: "))
s=[]
while n>0:
    r=n%10
    s.append(r)
    n=n//10
print(max(s))