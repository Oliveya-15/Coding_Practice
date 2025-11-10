# Permutations in which N people can occupy R seats
n=int(input("Enter number of people: "))
r=int(input("Enter no of seats: "))
f=1
j=n-r
for i in range(1,n+1):
    f=f*i
p=f/j
print(p)


# Example 1:
# Input: N = 5, r = 3
# Output: 60
# Explanation: To permute n people in r seats we have to find the value of n!/(n-r)!.The value of 5!/(5-3)! Is 60.

# Example 2:
# Input: N=6,r = 4.
# Output: 360