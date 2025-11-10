# Functions Problems :-

# Basic Function (Declaration)
def hello():
    print("Hello")
"""
Output : None
As we did not call the hello() function, that's why the instruction of printing 'Hello' will not execute.
"""

# Function Call (Along with function declaration)
def greet():
    print("Hello! Welcome to Python")
greet()
"""
Output : Hello! Welcome to Python
As we call the greet() function(line no. 14), the function greet() will print - Hello! Welcome to Python
"""

#Function with return type
def add(a, b):
    r = a + b   #OR,    return a + b
    return r           
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))

"""
Input  : a = 2, b = 3
Output : None
The return statement replaces the function call with the calculated value.
r have the value 5 (it can't be usble as function is not called andf used anywhere)We can use r later in our code which store (2+3 = 5)
For return: Console output is :- None (unless the returned value is printed by the caller)
"""

# calling the function and storing the result
def sum(n,m):              #OR,     def sum(n,m):    
    res=n+m                #             res = a + b 
    print(res)             #             print(res)
n=int(input("Enter n: "))  #        sum(2,3)
m=int(input("Enter m: "))
sum(n,m)
"""
Input  : n = 2, m = 3
Output : 5
"""

# Find the first digit from a number with Function 
def firstDigit(n):
    num=str(n)
    return (num[0])
"""
Input  : 123
Output : 1
By return : output will be 1
By print : output will be 1, None. 
"""






