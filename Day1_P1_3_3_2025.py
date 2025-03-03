#Day_1 P1
#Find the Smallest Number in an Array
a= list(map(int, input("enter the numbers: ").split()))
small=a[0]
for i in a:
    if i < small:
        small = i
print("the smallest element is: ",small)
