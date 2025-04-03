# Find the largest in the array
n = int(input("Enter the range: "))
a = list(map(int,input("Enter the numbers: ").split()))
l = a[0]
for i in range(n):
    if a[i] > l:
        l = a[i]
print(l)

"""
print(max(a))
"""



