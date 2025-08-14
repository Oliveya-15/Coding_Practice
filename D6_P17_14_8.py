#Day6 P17
#Sort Elements of an Array by Frequency
a=list(map(int,input("Enter the values: ").split()))
l1=[]
l={}
for i,val in enumerate(a):
    l[val]=a.count(val)
for k,v in l.items():
    for j in range(v):
        l1.append(k)
print(l1)
    
     
"""
Example 1:
Input: N = 8, array[] = {1,2,3,2,4,3,1,2}
Output: 2 2 2 1 1 3 3 4 
Explanation: Since  2 is present 3 times in an array , so print it 3 times ,then print ‘1’ 2 times and then ‘3’ 2 times and 4 has least frequency, it will be printed at last.

"""