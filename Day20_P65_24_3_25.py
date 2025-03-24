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



# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting we get 9,13,20,24,46,52


# Input: N = 5, array[] = {5,4,3,2,1}
# Output: 1,2,3,4,5
# Explanation: After sorting we get 1,2,3,4,5