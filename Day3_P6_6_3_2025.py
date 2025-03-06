n=int(input("Enter the range: "))
a = list(map(int,input("Enter the numbers: ").split()))
a.sort()
m = len(a) // 2
i = a[:m]
d = a[m:]
d.reverse()
r = i + d
print("The Arrange of array in increasing and decreasing order is: ",r)





# #Rearrange array in increasing and decreasing order
# Input: 8 7 1 6 5 9
# Output: 1 5 6 9 8 7
# Explanation: First three elements are in the ascending order and next three elements are in the descending order.

# Example 2:
# Input: 4 2 8 6 15 5 9 20
# Output: 2 4 5 6 20 15 9 8