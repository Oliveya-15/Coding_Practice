#Day_1 P1
#Find the Smallest Number in an Array

a = list(map(int,input("Enter the numbers: ").split()))
s=a[0]
for i in a:
    if i<s:
        s=i
print(s)

"""
Dry Run :-

a = 31, 6, 8, 2
s = a[0] s = 31
for i in a:
    i=31
    if i<s:
       31<31 : False (Continue loop)

    i=6
    if i<s:
       6<31 : True
       s=i   s=6 (Continue loop)

    i=8
    if i<s:
       8<6 : False (Continue loop)

    i=2
    if i<s:
       2<8 : True
       s=i   s=2 (Continue loop)

print(s)   Ans:- 2 (Smallest number in an array)  

"""