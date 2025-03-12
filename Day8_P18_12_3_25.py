#Replace elements by its rank in the array

n=int(input("Enter the range of the array: "))
a=list(map(int,input("Enter the numbers: ").split()))
o=[]
s=sorted(a)
for i in a:
    r = s.index(i)+1
    o.append(r)
print("The array Replace elements by its rank: ",o)

# Input: 20 15 26 2 98 6
# Output: 4 3 5 1 6 2
# Explanation: When sorted,the array is 2,6,15,20,26,98. So the rank of 2 is 1

"""
s=2,6,15,20,26,98
for i in a:
i=20
r=s.index(4)  / bcz s contain the sorted array in which 20's index position is 4
in o append the index value 4

keep on continue......

"""


