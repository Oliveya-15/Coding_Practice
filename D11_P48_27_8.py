#Day11 P48
#Program to Add two fractions
a=input("Enter the number: ")
b=input("Enter the number: ")
u1,d1 = a.split("/")
u2,d2 = b.split("/")
l=int(d1)*int(d2)
u=(int(u1)*int(d2))+(int(u2)*int(d1))
print(u,"/",l)


"""
a/b + c/d = (a*d)+(c*b) / (b*d)

Examples:

Example 1:
Input: 3/4 + 1/7 
Output: 25/28
Explanation: Since 3/4 + 1/7 = 25/28

Example 2:
Input: 5/2 +1/2
Output: 3/1
Explanation: Since 5/2 + 1/2 = 3/1
"""