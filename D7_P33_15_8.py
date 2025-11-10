#Day7 P33
#Greatest of 3 numbers
a=int(input("Enter value of A: "))
b=int(input("Enter value of B: "))
c=int(input("Enter value of C: "))
if (a>b) and (b>c):
    print("A is greatest")
elif (b>a) and (b>c):
    print("B is greatest")
else:
    print("C is greatest")
