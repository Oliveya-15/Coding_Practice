# Permutations in which N people can occupy R seats
n = int(input("Enter people value(n): "))
r = int(input("Enter seats value(r): "))
f=1
ff=1
n1 = n-r
for i in range(1,n+1):
    f=f*i
for j in range(1,n1+1):
    ff=ff*j
p = f/ff
print(p)



"""
What is a Permutation?
A permutation is an arrangement of objects in a specific order.
👉 Formula to find permutations of 𝑛 objects taken r at a time :
p = n! / (n-r)!

Factorial of 5! (5 factorial): 120
5-3 = 2 (n-r) so, factorial of 2 is (2!) : 2

p = n! / (n-r)!    so,    p = 120/2 = 60

"""
# Example 1:
# Input: N = 5, r = 3
# Output: 60
# Explanation: To permute n people in r seats we have to find the value of n!/(n-r)!.The value of 5!/(5-3)! Is 60.

# Example 2:
# Input: N=6,r = 4.
# Output: 360