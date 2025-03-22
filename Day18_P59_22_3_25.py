# Convert Binary to Decimal
n = int(input("Enter the number: "))
d,b=0,1
while n>0:
    r=n%10
    d=d+r*b
    n=n//10
    b=b*2
print(d)

"""
Initial values:
n = 100, d = 0, b = 1

1st Iteration (n = 100 > 0 is true)

r = n % 10 → r = 100 % 10 = 0
d = d + r * b → d = 0 + 0 * 1 = 0
n = n // 10 → n = 100 // 10 = 10
b = b * 2 → b = 1 * 2 = 2

2nd Iteration (n = 10 > 0 is true)

r = n % 10 → r = 10 % 10 = 0
d = d + r * b → d = 0 + 0 * 2 = 0
n = n // 10 → n = 10 // 10 = 1
b = b * 2 → b = 2 * 2 = 4

3rd Iteration (n = 1 > 0 is true)

r = n % 10 → r = 1 % 10 = 1
d = d + r * b → d = 0 + 1 * 4 = 4 :- Ans
n = n // 10 → n = 1 // 10 = 0
b = b * 2 → b = 4 * 2 = 8

print(d) => 4

"""


# Example 1:
# Input: N = 1011
# Output: 11
# Explanation: 1011 when converted to decimal number is “11”.

# Example 2:
# Input: 100
# Output: 4
# Explanation: 100 when converted to decimal number is “4”.