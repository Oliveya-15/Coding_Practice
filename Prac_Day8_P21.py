# Finding Equilibrium index in an array
a = list(map(int,input("Enter the values: ").split()))
a.sort()
m = len(a) // 2
v = a[m]
vi = a.index(v)
s = a[:vi+1]
r = sum(s)
print(r)