#Find prime numbers in a given range
n=int(input("Enter the starting value: "))
m=int(input("Enter the ending value: "))
o=[]
for i in range(n, m+1):  # Loop through numbers in range
    c = 0  # Reset counter for each number
    for j in range(1, i+1):  # Check divisibility from 1 to i
        if i%j==0:
            c+=1
    if c==2:
        o.append(i)
print("The Array with all the Prime numbers in this given range is: ",o)


"""
1st Outer Loop (i = 2)
c = 0
Inner Loop (j runs from 1 to 2)
j = 1: 2 % 1 == 0 → c = 1
j = 2: 2 % 2 == 0 → c = 2
c == 2, so 2 is prime → Add 2 to primes.
2nd Outer Loop (i = 3)
c = 0
Inner Loop (j runs from 1 to 3)
j = 1: 3 % 1 == 0 → c = 1
j = 2: 3 % 2 != 0 → (no change)
j = 3: 3 % 3 == 0 → c = 2
c == 2, so 3 is prime → Add 3 to primes.
3rd Outer Loop (i = 4)
c = 0
Inner Loop (j runs from 1 to 4)
j = 1: 4 % 1 == 0 → c = 1
j = 2: 4 % 2 == 0 → c = 2
j = 3: 4 % 3 != 0 → (no change)
j = 4: 4 % 4 == 0 → c = 3
c != 2, so 4 is NOT prime.
4th Outer Loop (i = 5)
c = 0
Inner Loop (j runs from 1 to 5)
j = 1: 5 % 1 == 0 → c = 1
j = 2: 5 % 2 != 0 → (no change)
j = 3: 5 % 3 != 0 → (no change)
j = 4: 5 % 4 != 0 → (no change)
j = 5: 5 % 5 == 0 → c = 2
c == 2, so 5 is prime → Add 5 to primes.
Continuing for i = 6 to i = 10
6 is NOT prime (c = 4)
7 is prime (c = 2) → Add 7 to primes
8 is NOT prime (c = 4)
9 is NOT prime (c = 3)
10 is NOT prime (c = 4)

"""


# Input: 2 10
# Output: 2 3 5 7 
# Explanation: Prime Numbers b/w 2 and 10 are 2,3,5 and 7.
