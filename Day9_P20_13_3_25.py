# Rotate array by K elements
n = int(input("Enter the range: "))
a = list(map(int,input("Eneter the numbers: ").split()))
k = int(input("Enter rotate position: "))
last = a[-k:]
first = a[0:-k]
r = last + first
print(r)

"""
a = 1,2,3,4,5,6,7
k=2
r = a[-k:] = [6,7]


"""



# Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
# Output: 6 7 1 2 3 4 5
# Explanation: array is rotated to right by 2 position .