# Reverse a given Array
n = int(input("Enter the range: "))
a = list(map(int,input("Enter the numbers: ").split()))
for i in range(n-1,-1,-1):
    print(a[i])