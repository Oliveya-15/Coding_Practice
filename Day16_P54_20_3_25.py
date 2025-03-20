# Program to Add two fractions
a=input("Enter the number: ")
b=input("Enter the number: ")

u1,d1 = a.split("/")
u2,d2 = b.split("/")

u1,d1,u2,d2 = int(u1),int(d1),int(u2),int(d2)

s1 = (u1*d2)+(u2*d1) 
s2 = (d1*d2)

print(s1,"/",s2)


"""
The basic formula of fraction addition is:

a/b + c/d = (a*d)+(c*b) / (b*d)

a=3,b=4
c=1,d=7

3/4 + 1/7 = (3*7)+(1*4) / (4*7)  
          = 21+4 / 28
          = 25/28

Take input as strings → "3/4" and "1/7".
Split at / to get numerators and denominators.
Convert to integers.

"""

# Example 1:
# Input: 3/4 + 1/7 
# Output: 25/28
# Explanation: Since 3/4 + 1/7 = 25/28

# Example 2:
# Input: 5/2 +1/2
# Output: 3/1
# Explanation: Since 5/2 + 1/2 = 3/1