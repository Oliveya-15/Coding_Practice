#Find all symmetric pairs in an array
n = int(input("Enter the range: "))
a = [list(map(int,input().split()))for _ in range(n)]
s=[]
for i in a:
    r=[i[1],i[0]]
    if r in a and r!=a and r not in s:
        s.append(i)
print("The new array is: ",s)


"""
a[[1,2],[3,4],[5,6],[2,1]]
i= a[  1  ,   2  ]
      i=0    i=1
r = i[1],i[0]
      2 ,  1
if r in a:
  does 2,1 exist in 'a' or not?
  2,1 exist in a = true, now check
if r!=a
  2,1 and 1,2 should be different then only it consider as symmetric = true, now check
if r not in a:
    2,1 should not be already exist in s[] otherwise s will get duplicate value = true
now add a[i] means [1,2] into s[]

this will continue repeat
    
"""


# Input: (1,2),(3,4),(5,6),(2,1)
# Output: (1,2)


#This way we can take user input of 2-D array :-
# n = int(input("Enter the number of rows: "))  
# a = []  # Initialize an empty list
# for _ in range(n):  
#     row = list(map(int, input().split()))  # Take space-separated input and convert to a list
#     a.append(row)  # Append the list (row) to a
#print("Your 2D array:", a)


#This we make in 1 line :-
#a = [list(map(int, input().split())) for _ in range(n)]

#This take only 2 element inside the child list :-
#a = [list(map(int, input().split()[:2])) for _ in range(n)]  # Ensures only 2 elements per row

