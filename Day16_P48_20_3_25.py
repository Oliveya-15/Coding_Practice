# Find LCM of two numbers
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
n1=a
n2=b
while b:
    a,b = b, a%b
lcm = n1*n2 / a
print(int(lcm))


"""
LCM(a,b) = a*b / GCD(a,b)

"""
# Example 1:
# Input: num1 = 4,num2 = 8
# Output: 8


# Example 2:
# Input: num1 = 3,num2 = 6
# Output: 6