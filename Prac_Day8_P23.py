# Check if array is subset of another array
a = list(map(int,input("Enter the values: ").split()))
b = list(map(int,input("Enter the values: ").split()))
if set(a).issubset(set(b)):
    print("a is subset of b")
elif set(b).issubset(set(a)):
    print("b is subset of a")
else:
    print("No Comparison")