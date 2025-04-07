# Find the median from the given array
n = int(input("enter the range: "))
a = list(map(int,input("enter the values: ").split()))
a.sort()
if n%2 == 1:
    m = a[n//2]
else:
    m1 = a[n//2-1]
    m2 = a[n//2]
    m = (m1+m2)/2
print(m)
        