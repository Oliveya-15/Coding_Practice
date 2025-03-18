#Greatest of three numbers
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of a: "))
c=int(input("Enter the value of c: "))
if a>b and b>c:
    print("A is the largest")
elif b>a and a>c:
    print("B is the largest")
else:
    print("C is the largest")


# Input: 1 3 5
# Output: 5
# Explanation: Answer is 5.Since 5 is greater than 1 and 3.