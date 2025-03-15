#Check if array is subset of another array
n=int(input("Enter the range for a1: "))
m=int(input("Enter the range for a2: "))
a1=list(map(int,input("Enter the numbers for a1: ").split()))
a2=list(map(int,input("Enter the numbers for a2: ").split()))
if set(a1).issubset(set(a2)):
    print("a1 is the subset of a2")
elif set(a2).issubset(set(a1)):
    print("a2 is the subset of a1")
else:
    print("No Match")

# Input: arr1[]= [1,3,4,5,2]
#        arr2[]= [2,4,3,1,7,5,15]
# Output: arr1[] is a subset of arr2[]
