#Day6 P18
#Rotate array by K elements
a=list(map(int,input("Enter the values: ").split()))
k=int(input("Enter the position for shift: "))
r=a[-k:]
l=a[:-k]
print(r+l)

"""
Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position .
"""