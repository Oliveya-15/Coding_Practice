#Day1 P4
##Count Frequency of each element in an array

a=list(map(int,input("Enter the numbers: ").split()))
r={}
for i in a:
    if i in r:
        r[i]+=1
    else:
        r[i]=1
print(r)

"""

Dry Run Example
Input:
Enter the Numbers: 2 3 2 5 2

a → [2, 3, 2, 5, 2]

f → {} (empty dictionary at start)

Iteration 1 → i = 2
2 in f? → ❌ (No)

else → f[2] = 1

f → {2: 1}

Iteration 2 → i = 3
3 in f? → ❌ (No)

else → f[3] = 1

f → {2: 1, 3: 1}

Iteration 3 → i = 2
2 in f? → ✅ (Yes, f[2] already exists)

f[2] += 1 → this means:

Look up the current value of f[2] (which is 1)

Add 1 → 1 + 1 = 2

Store 2 back into f[2]

f → {2: 2, 3: 1}

Iteration 4 → i = 5
5 in f? → ❌ (No)

else → f[5] = 1

f → {2: 2, 3: 1, 5: 1}

Iteration 5 → i = 2
2 in f? → ✅

f[2] += 1 → current value is 2, so 2 + 1 = 3

f → {2: 3, 3: 1, 5: 1}

Final Output:
{2: 3, 3: 1, 5: 1}

"""