# Express given number as Sum of Two Prime Numbers
n = int(input("Enter the number: "))
s=[]
c=0
found=False
for i in range(1,n+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        s.append(i)
for k in s:
    for m in s:
        if k+m == n:
            found=True 
if found:
    print("True")
else:
    print("False")


"""
👉 "Since both k and m are declared the same way (for k in s: and for m in s:),
 why does k take only one value at a time while m loops through the full list?"

The Key Reason:
🛑 k is in the outer loop, and m is in the inner loop.
🛑Nested loop formula: - the outer loop waits for the inner loop to finish before 
moving forward.

n = 10 

Start with an empty list s = [] to store prime numbers.
Loop through numbers from 1 to 10 (i runs from 1 to n).

Checking each i for primality:
i = 1: Factors are {1} → Not Prime → Not added to s.
i = 2: Factors are {1, 2} → Prime → Added to s, now s = [2].
i = 3: Factors are {1, 3} → Prime → Added to s, now s = [2, 3].
i = 4: Factors are {1, 2, 4} → Not Prime → Not added to s.
i = 5: Factors are {1, 5} → Prime → Added to s, now s = [2, 3, 5].
i = 6: Factors are {1, 2, 3, 6} → Not Prime → Not added to s.
i = 7: Factors are {1, 7} → Prime → Added to s, now s = [2, 3, 5, 7].
i = 8: Factors are {1, 2, 4, 8} → Not Prime → Not added to s.
i = 9: Factors are {1, 3, 9} → Not Prime → Not added to s.
i = 10: Factors are {1, 2, 5, 10} → Not Prime → Not added to s.
Final list of prime numbers up to 10:

s = [2, 3, 5, 7]

Step 2: Checking if Two Prime Numbers Sum to n (10)

Start with found = False.

Begin iterating through the prime numbers in s using two loops (k and m).

Loop Execution (k and m combinations):

k = 2, m = 2: 2 + 2 = 4, which is not 10. found remains False.

k = 2, m = 3: 2 + 3 = 5, which is not 10. found remains False.

k = 2, m = 5: 2 + 5 = 7, which is not 10. found remains False.

k = 2, m = 7: 2 + 7 = 9, which is not 10. found remains False.

k = 3, m = 2: 3 + 2 = 5, which is not 10. found remains False.

k = 3, m = 3: 3 + 3 = 6, which is not 10. found remains False.

k = 3, m = 5: 3 + 5 = 8, which is not 10. found remains False.

k = 3, m = 7: 3 + 7 = 10, which matches 10! found = True.

k = 5, m = 2: 5 + 2 = 7, which is not 10. found remains True.

k = 5, m = 3: 5 + 3 = 8, which is not 10. found remains True.

k = 5, m = 5: 5 + 5 = 10, which matches 10! found = True.

k = 5, m = 7: 5 + 7 = 12, which is not 10. found remains True.

k = 7, m = 2: 7 + 2 = 9, which is not 10. found remains True.

k = 7, m = 3: 7 + 3 = 10, which matches 10! found = True.

k = 7, m = 5: 7 + 5 = 12, which is not 10. found remains True.

k = 7, m = 7: 7 + 7 = 14, which is not 10. found remains True.

Since at least one valid pair (3+7 or 5+5) was found, found = True.

"""

# Example 1:
# Input : N = 74
# Output : True . 
# Explanation: 74 can be expressed as 71 + 3 and both are prime numbers. 

# Example 2:
# Input : N = 11
# Output : False. 
# Explanation: 11 cannot be expressed as sum of two prime numbers.