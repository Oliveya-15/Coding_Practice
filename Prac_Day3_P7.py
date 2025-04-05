#Sum of elements of the array
n = int(input("Enter the range: "))
a = list(map(int,input("Enter the values: ").split()))
s=0
for i in a:
    s=s+i
print(s)