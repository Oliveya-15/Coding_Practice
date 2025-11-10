#  Calculate the Area of the Circle
n=int(input("enter the n value: "))
r=22/7*(n*n)
r=str(r)
s=r[:r.index('.')+2]
print(s)
