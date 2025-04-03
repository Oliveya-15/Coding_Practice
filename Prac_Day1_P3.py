# Second Smallest & Second Largest element is the array
n =int(input("Enter the range: "))
a = list(map(int,input("enter the range: ").split()))
a.sort()
print("The Second Smallest number is",a[1])
print("The Second Largest number is",a[-2])
        

