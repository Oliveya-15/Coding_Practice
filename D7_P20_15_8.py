#Day7 P20
#Check if array is subset of another array
a=list(map(int,input("Enter the values: ").split()))
b=list(map(int,input("Enter the values: ").split()))
if set(a).issubset(set(b)):
    print("a is subset of b")
elif set(b).issubset(set(a)):
    print("b is subset of b")
else:
    print("Something Wrong")


"""Input: arr1[]= [1,3,4,5,2]
       arr2[]= [2,4,3,1,7,5,15]
Output: arr1[] is a subset of arr2[]"""