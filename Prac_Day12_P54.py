# Program to Add two fractions
a=input("Enter the number: ")
b=input("Enter the number: ")

a1,b1=a.split("/")
c,d=b.split("/")

u = (int(a1)*int(d)) + (int(c)*int(b1))
l = (int(b1)*int(d))

print(u,"/",l)


#(a*d)+(c*b) / (b*d)