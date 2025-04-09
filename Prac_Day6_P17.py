# Maximum Product Subarray in an Array
a = list(map(int,input("Enter the values: ").split()))
if len(a) == 1:
    print(a)
elif len(a) == 2:
    print(a[0]*a[1])
else:
    a.sort()
    m = (a[-1]*a[-2]*a[-3], a[0]*a[1]*a[-1])
    print(m)