#Day3 P8
#Find Median of the given Array
n=int(input("Enter the range: "))
a=list(map(int,input("Enter the values: ").split()))
a.sort()
m=len(a)//2
print(m)


"""
Example 1:
Input: [2,4,1,3,5]
Output: 3
"""