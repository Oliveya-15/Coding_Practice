# Convert Decimal to Binary Number
n=int(input("Enter the number: "))
b,base=0,1
while n>0:
    r=n%2
    b=b+r*base
    n=n//2
    base=base*10
print(b)

"""
bin() function used to convert decimal to binary it take input as integer
syntax: bin(number)   Returns a string that starts with '0b' (which indicates it is in binary format). => [0b100] : 4
to remove '0b'  use this statement   bin(decimal_number)[2:] => [100] : 4 

print(bin(n)[2:])"

Dry Run :-

n=4 b=0 base=1

4>0 : true
    r=4%2 = 0
    b=0+0*1 = 0
    n=4//2 = 2
    base=1*10 = 10
2>0 : true
    r=2%2 = 0
    b=0+0*10 = 0
    n=2//2 = 1
    base=10*10 = 100
1>0 : true
    r=1%2 = 1                       2 ) 1 ( 0  <-- quotient
    b=0+1*100 = 100                   - 0
    n=1//2 = 0                        ----
    base=100*10 = 1000                  1  <-- Remainder
    
0>0 : False

print(b) => 100 : 4

"""

# Example 1:
# Input: N = 15
# Output: 1111
# Explanation: 15 in binary is represented as "1111".

# Example 2:
# Input: 18
# Output: 10010
# Explanation: 18 in binary is represented as "10010".