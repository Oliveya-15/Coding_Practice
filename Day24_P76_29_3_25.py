# Reverse a String
a = input("Enter the String: ")
b=a[::-1]
print(b)

"""
Below are the different methods by which we can perform this :-

Method 1 :
b=reversed(a)
print("".join(b))

Method 2 :
b=a[::-1]

Method 3 :
for i in reversed(a):
    print(i)

Method 4 :
for i in range(len(a)-1,-1,-1):
    print(a[i])

"""


# Input : Hello
# Output: olleH