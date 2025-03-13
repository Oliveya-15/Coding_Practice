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
last = a[-k:] => [6,7]   
bcz, -k start from backwards and as k value is 2 so it will start from -2 which have 6 then it will take 7 like this
first = a[0:-k] => [1,2,3,4,5] take from 0th position till -k position which starts from 1 to 5
add last + first => [6,7,1,2,3,4,5]

"""



# Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
# Output: 6 7 1 2 3 4 5
# Explanation: array is rotated to right by 2 position .