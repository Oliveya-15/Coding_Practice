#Average of all the elements in the array
n = int(input("Enter the range of the array: "))
a = list(map(int,input("Enter the Numbers: ").split()))
s = 0
for i in a:
    s = s+i
    o = s/n
print("Average of all the elements is: ",o)