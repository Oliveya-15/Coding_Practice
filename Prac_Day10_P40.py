# Print Fibonacci Series up to Nth term
n = int(input("Enter the range: "))
a,b=0,1
print(a,b,end="")
for i in range(n+1 - 2):
    c=a+b
    print(c,end="")
    a,b=b,c