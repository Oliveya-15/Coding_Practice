# Print Fibonacci Series up to Nth term
n = int(input("Enter the range: "))

# First two terms
a, b = 0, 1

# Print first two terms
print(a, b, end=" ")

# Generate Fibonacci series up to n terms
for i in range(n+1 - 2):  # Already printed first 2 terms
    c = a + b
    print(c, end=" ")
    a, b = b, c  # Update values for the next iteration

"""
Step 1:
Start with a = 0, b = 1
Compute c = a + b = 0 + 1 = 1
Now update the values:
a takes the value of b → a = 1
b takes the value of c → b = 1
So now, a = 1, b = 1
Step 2:
Compute c = a + b = 1 + 1 = 2
Update:
a = b → a = 1
b = c → b = 2
Now, a = 1, b = 2
Step 3:
Compute c = a + b = 1 + 2 = 3
Update:
a = b → a = 2
b = c → b = 3
Now, a = 2, b = 3
Step 4:
Compute c = a + b = 2 + 3 = 5
Update:
a = b → a = 3
b = c → b = 5
Now, a = 3, b = 5

# Why n - 2?
The first two Fibonacci numbers (0 and 1) are already printed.
We only need to calculate the remaining n-2 terms.
n = 5
We need 5 Fibonacci numbers:
0, 1, 1, 2, 3, 5
First two terms (0 and 1) are already known.
The remaining (5 - 2 = 3) terms (1, 2, 3) must be generated in the loop.
The loop should run 3 times to generate those numbers.

# a stores the previous Fibonacci number.
# b stores the current Fibonacci number.
# c = a + b calculates the next Fibonacci number.

"""


# Input: N = 5
# Output: 0 1 1 2 3 5
# Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)
