# Replace elements by its rank in the array
a = list(map(int,input("Enter the values: ").split()))
a.sort()
for i,val in enumerate(a):
    print(val,i)