#Day8 P37
#Print Fibonacci Series up to Nth term
n=int(input("Enter the range: "))
a,b=0,1
print(a,b,end=" ")
for i in range(2,n+1):
    c=a+b
    print(c,end=" ")
    a,b=b,c
