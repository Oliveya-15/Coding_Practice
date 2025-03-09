# Rotate array by K elements : Block Swap Algorithm
n = int(input("Enter the range: "))
a = list(map(int,input("enter The Numbers: ").split()))
k = int(input("Enter the reverse value: "))
f=[]
m = a[:k] 
a = a[k:]
f = a+m
print("The new array is: ",f)


# Input: N = 5, array[] = {1,2,3,4,5} K=2
# Output: {3,4,5,1,2}
# Input: N = 7, array[] = {1,2,3,4,5,6,7} K=3
# Output: {4,5,6,7,1,2,3}

