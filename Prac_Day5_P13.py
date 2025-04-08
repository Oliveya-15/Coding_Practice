# Adding element in an array
a = list(map(int,input("Enter the values: ").split()))
n=len(a)
a.insert(0,23)   # insert at beginning
a.insert(n+1,45) # insert at last
a.insert(3,67)   # insert at specific position
print(a)