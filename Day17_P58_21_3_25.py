# Program to Find Roots of a quadratic equation
import math

# Input values
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Calculate the discriminant (D)
D = b**2 - 4*a*c  

# Check the nature of roots
if D > 0:
    root1 = (-b + math.sqrt(D)) / (2 * a)
    root2 = (-b - math.sqrt(D)) / (2 * a)
    print("Roots are real and different:", root1, ",", root2)
elif D == 0:
    root = -b / (2 * a)
    print("Roots are real and equal:", root)
else:
    real_part = -b / (2 * a)
    imag_part = math.sqrt(-D) / (2 * a)
    print("Roots are complex:", real_part, "+ i", imag_part, ",", real_part, "- i", imag_part)


# Example 1:
# Input: a = 1, b = -3, c = -10
# Output: Roots are real and different, i.e(5 , -2).

# Example2:

# Input: a = 1, b = 1, c = 1
# Output: Roots are complex, i.e-(-0.5+i1.732 , -0.5-i1.732).