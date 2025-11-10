# Selection Sort Algorithm
n = int(input("Enter the range: "))
a = list(map(int,input("Enter the numbers: ").split()))
for i in range(n-1):
    min=a[i]
    loc=i
    for j in range(i+1,n):
        if (min>a[j]):
            min=a[j]
            loc=j
    t=a[i]
    a[i]=a[loc]
    a[loc]=t
print(a)

# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

# Example 2:
# Input: N=5, array[] = {5,4,3,2,1}
# Output: 1,2,3,4,5
# Explanation: After sorting the array is: 1, 2, 3, 4, 5