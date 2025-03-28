# Bubble Sort Algorithm
n = int(input("Enter the range: "))
a = list(map(int,input("enter the numbers: ").split()))
for i in range(n-1):
    ptr=0
    while(ptr<n-1):
        if(a[ptr]>a[ptr+1]):
            t=a[ptr]
            a[ptr]=a[ptr+1]
            a[ptr+1]=t
        ptr+=1
print(a)


"""
a = [8, 4, 3, 7, 2]
n = 5

Outer Loop Starts (for i in range(n-1))
The outer loop runs n-1 = 4 times (from i = 0 to i = 3).
it continue n-1 times means for 5 value it execute 4 time because, in 4 time only the sorting become done there is no need to perform the loop for 5 times because, in each step number get sorted correctly in 4 time iteration

First Outer Loop Iteration (i = 0)
Initial list before this iteration: [8, 4, 3, 7, 2]

Inner Loop (while ptr < n-1)
ptr will run in each i'th position value            ptr=a[0] = 8, a[ptr+1 = 0+1 = 1] = 4                               
ptr is a variable that starts at 0.                                                 
n-1 means that ptr will loop until it reaches the second last index of the list.
ptr increases in every iteration (ptr += 1).
ptr starts at 0 and moves through the list comparing adjacent elements.

ptr = 0: Compare a[0] = 8 and a[1] = 4
Since 8 > 4, swap → [4, 8, 3, 7, 2]
ptr = 1: Compare a[1] = 8 and a[2] = 3
Since 8 > 3, swap → [4, 3, 8, 7, 2]
ptr = 2: Compare a[2] = 8 and a[3] = 7
Since 8 > 7, swap → [4, 3, 7, 8, 2]
ptr = 3: Compare a[3] = 8 and a[4] = 2
Since 8 > 2, swap → [4, 3, 7, 2, 8]
After the first iteration, the largest number 8 is at the correct position.



Third Outer Loop Iteration (i = 2)
Initial list before this iteration: [3, 4, 2, 7, 8]

Inner Loop
ptr = 0: Compare a[0] = 3 and a[1] = 4
No swap needed.
ptr = 1: Compare a[1] = 4 and a[2] = 2
Since 4 > 2, swap → [3, 2, 4, 7, 8]
After the third iteration, the third-largest number 4 is at its correct position.



Fourth Outer Loop Iteration (i = 3)
Initial list before this iteration: [3, 2, 4, 7, 8]

Inner Loop
ptr = 0: Compare a[0] = 3 and a[1] = 2
Since 3 > 2, swap → [2, 3, 4, 7, 8]

After the fourth iteration, the smallest element 2 is also in its correct position, and the list is fully sorted.
"""


# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting we get 9,13,20,24,46,52


# Input: N = 5, array[] = {5,4,3,2,1}
# Output: 1,2,3,4,5
# Explanation: After sorting we get 1,2,3,4,5


