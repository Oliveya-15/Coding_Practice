# Search an element in an array
a = list(map(int,input("Enter the values: ").split()))
i = int(input("Enter the item for search: "))
c = 0
if i in a:
    c=+1
if c>0:
    print("Item found")
else:
    print("Item not found")