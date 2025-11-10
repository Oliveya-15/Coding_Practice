# Basics of Python :-

#Printing in python " "
print("Hello World !")

#printing in python ' '
print ('Oliveya')

#Concatenation of strings
print("This is" + ' Me')

#Use of end : to keep all texts in one line or add element add the end of the line
print("Hello",end=" ")
print("World")

#Use of end \n : shift the text into next line(\n)
print("One",end=",")
print("Hello\nWorld")

#Printing a word for multiple time in a single line
"""
range(stop)    |      range(start,stop)     |      range(start,stop,step)
for i in n:   n should be any list,set,tuple etc.   use for 'iterable'.  use for list,tuple,dict,set.  Iterate n number of element
for i in range(n):   n must be an integer.   use for 'evaluation',   For looping a particular element n no. of times.
"""
x="Oliveya"
num=5
for i in range(num):
    print(x,end="")

# Write your code below that prints a a times and b b times, seperated by c
a,b,c="6""4""&"
for i in range(int(a)):
    print(a,end="")
print(c,end="")
for j in range(int(b)):
    print(b,end="")
""" 
In one line solution :- print(a*int(a)+c+b*int(b))
a*int(a)  :-  a is string "6" * int(6)
          =   a * 6 ->  "6" * 6  =>  666666
"""

#Taking user input
v1=input("Enter anything: ")
v2=int(input("Enter integer: "))
v3=float(input("Enter integer: "))
print(v1,v2,v3)

"""
#Python Fundamentals Coding Practice Problems
1=>   ARITHMATIC OPERATOR
x=int(input())
y=int(input())
#code here
# Perform addition x+y below
p = x+y
# Perform subtraction x-y below
q = x-y
# Perform multiplication x*y below
r = x*y
# Perform integer divison x//y below             l,k=18,6
s = x//y                                         print(l/k)   =>  3.0
# Perform modulo operation x%y below             print(l//k)  =>  3
t = x%y
print(p, q, r, s, t)

Input: x = 1, y = 2
Output: 3 -1 2 0 1 
Explanation: The given operations are performed.

2=>  LOGICAL OPERATOR
a=int(input())
b=int(input())
#code here
p = a and b
#Do a or b below
q = a or b
#Do not a below
r = not a
#The code below prints the output. Don't change it!
print(p,q,r)     

Input: a = 0, b = 2
Output: 0 2 True
Explanation: 0 and 2 gives 0. 0 or 2 gives 2. not 0 give True as 0 is False.

3=>  BITWISE OPERATOR
a=int(input())
b=int(input())
c=int(input())
#code here
#Do a^a below
d= a^a
#Do c^b below
e= c^b
#Do a&b below
f= a&b
#Do c|(a^a) below
g= c | (a^a)
#Do ~e below
e= ~e
print(d, e, f, g)

Input: a = 1, b = 2, c = 3
Output: 0 -2 0 3
Explanation: We print d e f g after performing the given operations.

4=>  TYPE CONVERSION
d = float(input())
#code here
print(int(d))

Input: d = 10.23
Output: 10
Explanation: The integer value of 10.23 is 10

5=>  SWAPPING
a = int(input())
b = int(input())
a,b=b,a
or, (Using third variable)
c=a
a=b
b=c
print(a,b)

Input: a = 1, b = 2
Output: 2 1
Explanation: Initially a = 1 and b = 2, now a = 2 and b = 1.

6=>  Geometric Progression Term
a = int(input())
n = int(input())
r = 2
ans = a*pow(r,n-1)
or,
result = a * (r ** (n - 1))
print(ans)

Input: a = 2, n = 10
Output: 1024
Explanation: an = a * r(n-1) = 2 * 210-1 = 1024

"""




