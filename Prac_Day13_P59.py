# Convert Binary to Decimal
b = int(input("Enter the value: "))
d,base=0,1
while b>0:
    r=b%10
    d=d+r*base
    b=b//10
    base=base*2
print(d)
