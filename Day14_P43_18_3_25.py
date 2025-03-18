# Factors of a Given Number
n=int(input("Enter the number: "))
for i in range(1,n+1):
    if n%i == 0:
        print(i,end=" ")

# Input: n = 6
# Output: 1,2,3,6
# Explanation: 6 is divisible by 1,2,3,6