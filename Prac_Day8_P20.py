# Rotate array by K elements left-right
a = list(map(int,input("Enter the values: ").split()))
k = int(input("Enter k value: "))
l = a[-k:]
r = a[:-k]
r = (l+r)
print(r)