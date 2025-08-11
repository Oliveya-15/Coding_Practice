#Day3 P7
#Rotate array by K elements : Block Swap Algorithm
n=int(input("Enter the range: "))
l=list(map(int,input("Enter the values: ").split()))
k=int(input("Enter the Position: "))
s=l[:k]
s1=l[k:]
print(s1+s)



"""
Input: N = 5, array[] = {1,2,3,4,5} K=2
Output: {3,4,5,1,2}
Explanation: Rotate the array to right by 2 elements.
"""