#Day5 P15
#Find all Symmetric Pairs in the array of pairs
n=int(input("Enter how many pairs you want: "))
a = [list(map(int,input("Enter the values: ").split()[:2]))for _ in range(n)]
s=[]
for i in a:
    r=[i[1],i[0]]
    if r in a and r != a and r not in s:
        s.append(i)
print(s)
        
"""
Example 1:
Input: (1,2),(2,1),(3,4),(4,5),(5,4)
Output: (2,1) (5,4)
Explanation: Since (1,2) and (2,1) are symmetric pairs and (4,5) and (5,4) are symmetric pairs.
"""