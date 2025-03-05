#Day1 P2
#Find the Largest from an Array
a=list(map(int, input("Enter the numbers: ").split()))
large=a[0]
for i in a:
    if i > large:
        large=i
print("The Largest element is: ",large)
