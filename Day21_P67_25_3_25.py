# Insertion Sort algorithm
n=int(input("Enter the range: "))
a=list(map(int,input("Enter the values: ").split()))
for i in range(1,n):
    temp=a[i]
    j=i-1
    while ((a[j]>temp) and (j>=0)):
        a[j+1]=a[j]
        j-=1
    a[j+1]=temp
print(a)

# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

# Example 2:
# Input: N=5, array[] = {5,4,3,2,1}
# Output: 1,2,3,4,5
# Explanation: After sorting the array is: 1, 2, 3, 4, 5