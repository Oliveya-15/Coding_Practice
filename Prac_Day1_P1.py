# Find the smallest in the array
n = int(input("Enter the range: "))
a = list(map(int,input("Enter the numbers: ").split()))
s = a[0]
for i in range(n):
    if a[i]<s:
        s=a[i]
print(s)


"""
print(min(a))
"""


"""
n =3
a = 56 78 2

s = a[0]  => s = 56
for i in range(n):
    a[i] < s:
    a[0]=56 < 56 : False
    No change

    a[i] < s:
    a[1]=78 < 56 : False
    No chnage

    a[i] < s:
    a[2]=2 < 56 : True
        s = a[i] => a[2] = 2
        s = 2    :- Ans
"""