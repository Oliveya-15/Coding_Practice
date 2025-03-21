#  Calculate the Area of the Circle
n = int(input("Enter the value: "))
a = 22/7*(n*n)
a1 = (a * 10) // 1 / 10
print(a1)

"""
Method 1:    (n * 10) // 1 / 10  => Removes extra decimals
             from 78.57142857142857  we got until 78.5

Method 2:    s = str(n)  # Convert to string
             r = s[:s.index('.') + 2]  # Keep only one digit after decimal

"""
# Example 1:
# Input: N = 5
# Output: 78.5
# Explanation: Using formula  πr2 for finding area of circle we get area as 78.5

# Example 2:
# Input: N = 4
# Output: 50.2
# Explanation: Using formula  πr2 for finding area of circle we get area as 50.2