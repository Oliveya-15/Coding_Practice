# Convert Decimal to Binary Number
d = int(input("enter the decimal value: "))
b,base=0,1
while d>0:
    r=d%2
    b=b+r*base
    d=d//2
    base=base*10
print(b)