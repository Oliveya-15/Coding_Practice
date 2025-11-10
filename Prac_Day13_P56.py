# Express given number as Sum of Two Prime Numbers
n = int(input("Enter the number: "))
f=[]
for i in range(1,n+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        f.append(i)
for k in f:
    for m in f:
        if k+m==n:
            found=True
if found:
    print("True")
else:
    print("False")


# Example 1:
# Input : N = 74
# Output : True . 
# Explanation: 74 can be expressed as 71 + 3 and both are prime numbers. 

# Example 2:
# Input : N = 11
# Output : False. 
# Explanation: 11 cannot be expressed as sum of two prime numbers.