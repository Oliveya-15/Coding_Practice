#Day1 P2
#Find the Largest from an Array

a = list(map(int,input("Enter the numbers: ").split()))
l=a[0]
for i in a:
    if i>l:
        l=i
print(l)

"""
Dry Run:-

a = 2,71,45,90
s=a[0] s=2

for i in a:

    i=2
    if i>l:
       2>2: False (Continue Loop)
    
    i=71
    if i>l:
       71>2: True
       l=i  l=71  (Continue loop)
    
    i=45
    if i>l:
       45>71: False (Continue Loop)

    i=90
    if i>l:
       90>71: True
       l=i  l=90  (Continue loop)

print(l)  Ans:- 90
       
"""