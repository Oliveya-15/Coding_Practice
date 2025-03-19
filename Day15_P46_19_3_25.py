# Check if a number is Automorphic Number
n = int(input("Enter the number: "))
s = n*n
l=str(s)[-2:]

if(n == int(l)):
    print("Automorphic Number")
else:
    print("Not a Automorphic Number")

"""
slicing  only works on sequences like -  strings, lists, and tuples
if s=5776 if i do s[-2:] it will give error as s is an integer for that we need to 
convert s into string using     =>       str(s)[-2:]

in if-else conditional statements we can't comapre (string == integer) it will give 
error/wrong output example    s=76(in string)   n=76(in integer)   if i do     if(n == s)  
it will return false/wrong output  so for this case type cast it like    =>    if(n == int(l)):

"""


# Input Format: N = 76
# Result: Automorphic Number
# Explanation: Calculating 76 * 76 gives 5776, it ends with the given number.