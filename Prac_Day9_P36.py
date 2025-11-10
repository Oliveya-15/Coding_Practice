# Greatest of three numbers
a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
c = int(input("Enter value of C: "))
if a>b and a>c:
    print("A is greatest")
elif b>c and b>a:
    print("B is greatest")
else:
    print("C is greatest")