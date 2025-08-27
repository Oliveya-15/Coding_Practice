#Day11 P50
#Express given number as Sum of Two Prime Numbers
n=int(input("Enter the number: "))
l=[]
t=False
for i in range(1,n+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        l.append(i)
for k in l:
    for m in l:
        if k+m == n:
            t=True
if t:
    print("True")
else:
    print("False")