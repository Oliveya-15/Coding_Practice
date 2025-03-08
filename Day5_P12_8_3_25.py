#Adding Element in an array
n=int(input("Enter the range: "))
a=list(map(int,input("Enter the numbers: ").split()))
b=int(input("Enter the new element: "))
a.append(b)
print("The new array is: ",a)