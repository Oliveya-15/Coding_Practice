#Day5 P16
#Replace elements by its rank in the array
a=list(map(int,input("Enter the values: ").split()))
l=[]
s=sorted(a)
for i in a:
    l.append(s.index(i)+1)
print(l)


"""
Example 1:
Input: 20 15 26 2 98 6
Output: 4 3 5 1 6 2
Explanation: When sorted,the array is 2,6,15,20,26,98. So the rank of 2 is 1,rank of 6 is 2,rank of 15 is 3 and so…
"""