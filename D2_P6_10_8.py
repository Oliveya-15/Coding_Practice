#Day2 P6
#Calculate Sum of the Elements of the Array

"""a=list(map(int,input("Enter the values: ").split()))
s=0
for i in a:
    s=s+i
print(s)"""

n=int(input("Enter the range: "))
l=list(map(int,input("Enter the numbers: ").split()))
s=0
for i in range(n+1):
    s=s+i
print(s)
