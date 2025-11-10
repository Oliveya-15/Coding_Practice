#Find GCD of two numbers
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
f=[]
f1=[]
f2=[]
for i in range(1,a+1):
    if a%i==0:
        f.append(i)
for j in range(1,b+1):
    if b%j==0:
        f1.append(j)
for m,val in enumerate(f):
    for n,value in enumerate(f1):
        if val==value:
            f2.append(val)
print(max(f2))



# Input:N1 = 9, N2 = 12
                
# Output:3
# Explanation:Factors of 9: 1, 3 and 9
# Factors of 12: 1, 2, 3, 4, 6, 12
# Common Factors: 1, 3 out of which 3 is the greatest hence it is the GCD.