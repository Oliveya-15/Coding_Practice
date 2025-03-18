#Print all Prime Factors of the given number
n=int(input("Enter the number: "))
for i in range(2,n+1):
    if n%i == 0:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)
        
"""

1️⃣ Incorrect Prime Check in Your Code
❌ Mistake:

if (i % 1 == 0) and (i % i == 0):
🔹 This condition is always true for any number.

✅ Correction:
To check if i is prime, it should not be divisible by any number except 1 and itself.

for j in range(2, i):
    if i % j == 0:
        break  # i is not prime
🔹 Why?
Because a prime number must not have any divisors other than 1 and itself.

2️⃣ Printing the Prime Factor Inside the Loop
❌ Mistake:

for j in range(2, i):
    if i % j == 0:
        break
    else:
        print(i)  # ❌ Wrong position
🔹 This prints i multiple times inside the loop.

✅ Correction:
Move print(i) outside the inner loop:

for j in range(2, i):
    if i % j == 0:
        break
else:
    print(i)
🔹 Why?
Because we only print i if no divisor is found after checking all possible values.

3️⃣ Correct Range for Loops
❌ Mistake:

for i in range(1, n + 1):  # ❌ Starts from 1 (1 is not prime)
✅ Correction:
Start the loop from 2, because 1 is not a prime number.

for i in range(2, n + 1):  
🔹 Why?
Prime numbers start from 2, so there's no need to check 1.

4️⃣ Using else After the for Loop
✅ What You Learned:

The else in a for loop only executes if the loop completes without break.
This is a simple and clean way to check for prime numbers.

for j in range(2, i):
    if i % j == 0:
        break
else:
    print(i)  # Only prints if `i` is prime

"""


# Input: N=60
# Output: 2, 3, 5
# Explanation: All factors/divisors of 60 include: 1, 2, 3, 4, 5, 6, 10, 12, 18, 20, 30, 60. Out of these only 2, 3 and 5 are prime."
