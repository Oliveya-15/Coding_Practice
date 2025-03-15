#Search an Element in an Array 
n=int(input("Enter the range: "))
a=list(map(int,input("Enter the numbers: ").split()))
item=int(input("Enter the item to search: "))
c=0
for i in a:
    if i == item:
        print(a.index(i))
        c=c+1
if c==0:
    print("Item not found")
    


# Input: a[] = {1,2,3,4,5} k=3                                                                              
# Output: 2                                                                                                              
# Explanation: The answer is 2 because 3 is present at 2nd index.