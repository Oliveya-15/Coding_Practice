# Average of all element in array
n = int(input("Enter the range: "))
a = list(map(int,input("Enter the numbers: ").split()))
s=0
for i in a:
    s=s+i
    avg=s/n
print(avg)