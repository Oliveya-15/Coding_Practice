#Check if a number is Perfect Number or not
n=int(input("Enter the Number: "))
p=0
for i in range(1,n):
    if n%i==0:
        p=p+i
if p==n:
    print("The Number is Perfect: ",n)
else:
    print("The Number is not Perfect: ",n)


"""
Dry Run for n = 6
Start: p = 0
Loop Iterations:

i = 1: 6 % 1 == 0 → p = 0 + 1 = 1
i = 2: 6 % 2 == 0 → p = 1 + 2 = 3
i = 3: 6 % 3 == 0 → p = 3 + 3 = 6
i = 4: 6 % 4 != 0 → No change (p = 6)
i = 5: 6 % 5 != 0 → No change (p = 6)
Final Check: p == 6 ✅
Output: "The Number is Perfect: 6"

"""

# Input: 6
# Output: 6 is a Perfect Number because 1 + 2 + 3 = 6 (sum of its proper divisors).






