# Rotate array by k element - Block awep algorithm
n = int(input("Enter the range: "))
a = list(map(int,input("Enter the values: ").split()))
k = int(input("Enter k value: "))
s = a[k:]
s1 = a[:k]
print(s+s1)