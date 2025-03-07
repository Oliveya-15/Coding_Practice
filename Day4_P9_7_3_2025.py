#Find the Median of the given array
n = int(input("Enter the range: "))
a = list(map(int,input("Enter the Numbers: ").split()))
a.sort()
if n%2 == 1:
    m = a[len(a) // 2]
else:
    m1 =  a[len(a) // 2 - 1]
    m2 = a[len(a) // 2]
    m = (m1+m2) / 2                                                                                                                                                                                                                                                                                                                  
print("The median of the array is: ",m)