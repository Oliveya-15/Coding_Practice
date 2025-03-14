#Finding Equilibrium index in an array
n=int(input("Enter the range: "))
a=list(map(int,input("Enter the numbers: ").split()))
right=[]
right1=[] 
left1=[]
for idx, i in enumerate(a):
    if idx==0:
        left=0
        right=a[idx+1:n]
        right=sum(right)
        if left == right:
            print(idx)
    elif idx>0:
        left1=a[:idx]   
        left1=sum(left1)
        right1=a[idx + 1:]
        right1=sum(right1)
        if left1 == right1:
            print(idx)


"""
a= [2,3,-1,8,4] output => 3
Index	Element	    Left Sum (before)	               Right Sum (after)
 0	       2	       0	                        3 + (-1) + 8 + 4 = 14
 1	       3	       2	                        -1 + 8 + 4 = 11
 2        -1	     2 + 3 = 5	                     8 + 4 = 12
 3	       8	     2 + 3 + (-1) = 4	             4 = 4 ✅ (Match!)
 4	       4	     2 + 3 + (-1) + 8 = 12	         0

"""

"""
DRY RUN :-

for idx, i in enumerate(a):      idx=[0], i=[2]   : here idx repersent index[0] and i reperest the value which the index have[2]
    if idx==0:                   idx==0 : true
        left=0                   left = 0
        right=a[idx+1:n]         right = [3,-1,8,4]  we take idx+1 bcz, idx=0 i=[2] to take all the right value we have to start from 2nd position so idx+1 [0+1=1] so idx=[1] and i=[3] to n
        right=sum(right)         right = 3 + (-1) + 8 + 4 = 14
        if left == right:        left == right:   0 != 14   don't print index else, if match occur print current index
            print(idx)
    elif idx>0:                  idx>0: true as idx[1], i=[3]
        left1=a[:idx]            left1=[2]
        left1=sum(left1)         left1=[2]
        right1=a[idx + 1:]       right1=[-1,8,4]
        right1=sum(right1)       right1=[-1 + 8 + 4 = 11]
        if left1 == right1:      left1 == right1 : false   2 != 11   don't print
            print(idx)

keep on continue........

"""


# Input: nums = [2,3,-1,8,4]
# Output: 3
# Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
# The sum of the numbers after index 3 is: 4 = 4

