#Day10 P46
#Find the sum of numbers in the given range
n=int(input("Enter the starting range: "))
m=int(input("Enter the ending range: "))
s=0
for i in range(n,m+1):
    s=s+i
print(s)