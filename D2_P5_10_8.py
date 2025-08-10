#Day2 P5
#Rearrange array in increasing-decreasing order

a=list(map(int,input("Enter the values: ").split()))
a.sort()
n=len(a)//2
first=a[:n]
last=a[n:]
first.sort()
last.reverse()
print(first+last)


"""
Example 1:
Input: 8 7 1 6 5 9
Output: 1 5 6 9 8 7
"""

