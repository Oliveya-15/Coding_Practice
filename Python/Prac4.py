# RECURSION :-

# Print 1 To N Without Loop
x=int(input("Enter the range: "))
def loop(y):
    if (y==0):
        return
    else:
        loop(y - 1)
        print(y,end=" ")
loop(x)

"""
Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10

👉 It prints numbers from 1 to x (whatever you entered)
👉 It uses recursion (a function calling itself again and again).

Example:
You tell your friend,

“Count 3 for me!”
Your friend says:
“Wait, I’ll first ask another friend to count 2 for me.”
That friend says:
“Wait, I’ll ask another friend to count 1 for me.”
That last friend says:
“I’ll just say 1!”
Then each friend, one by one, says their number while returning back.

Result: 1 2 3

loop(3) is called
➡️ y = 3
Not zero → it calls loop(2) first

Step 2

loop(2) is called
➡️ y = 2
Not zero → it calls loop(1) first

Step 3

loop(1) is called
➡️ y = 1
Not zero → it calls loop(0) first

Step 4

loop(0) is called
➡️ y = 0
It returns (stops here)

Now the function starts coming back step by step.

## Coding DRY RUN :

🟩 Step 1 — Program starts

Python reads your code line by line.

1️⃣ x = int(input(...))
👉 You type 3, so now x = 3.

2️⃣ Python defines the function loop(y), but does not run it yet.
It just stores it in memory.

3️⃣ The last line loop(x) is executed → so Python runs loop(3).

🟩 Step 2 — First call: loop(3)

Now Python goes inside the function:

def loop(y):
    if y == 0:
        return
    else:
        loop(y - 1)
        print(y, end=" ")


🧩 Here y = 3.

Python checks if y == 0: → ❌ No, it’s 3.

Goes to the else: part.

Executes loop(y - 1) → that means loop(2).

So now Python pauses the current function (loop(3)), and starts a new function call → loop(2).

🟩 Step 3 — Second call: loop(2)

New function frame in memory.

Now y = 2.

Checks if y == 0: → ❌ No.

Goes to loop(y - 1) → calls loop(1).

🧠 Now loop(2) is paused too, waiting for loop(1) to finish.

🟩 Step 4 — Third call: loop(1)

New function frame again.

Now y = 1.

Checks if y == 0: → ❌ No.

Calls loop(y - 1) → so loop(0).

🟩 Step 5 — Fourth call: loop(0)

Now y = 0.

Checks if y == 0: → ✅ Yes → so it hits return.

That means: stop here and go back to whoever called you (which is loop(1)).

No printing yet!

🟦 Now Python “comes back” (returns)

Here’s how it unwinds 👇

🔙 Back to loop(1)

The line loop(y - 1) is done.

Now executes print(y, end=" ")
👉 prints 1.

🔙 Back to loop(2)

Its recursive call is done.

Now prints 2.

🔙 Back to loop(3)

Its recursive call is done.

Now prints 3.

loop(3)
  └─ calls loop(2)
       └─ calls loop(1)
            └─ calls loop(0)
                 └─ returns immediately (base case)
            └─ now print(1)
       └─ now print(2)
  └─ now print(3)
Dry run — example with x = 3
I’ll show the sequence of calls and when each print happens.
Program starts and you enter 3.

loop(3) is called.
loop(3) → since 3 != 0, it calls loop(2).
loop(2) → calls loop(1).
loop(1) → calls loop(0).
loop(0) → hits base case and returns immediately (prints nothing).
Back to loop(1) after loop(0) returned → print(1, end=" ") → outputs 1.
Back to loop(2) after loop(1) returned → print(2, end=" ") → outputs 2.
Back to loop(3) after loop(2) returned → print(3, end=" ") → outputs 3.
"""

# Fibonacci series up to Nth term (Applicable with highest Numbers as well)
n1 = int(input("Enter the range: "))
def fibo(n):
    m=1000000007
    if n==0:
        return [0]
    elif n==1:
        return [0,1]
    f=[0,1]
    for i in range(2,n+1):
        num=(f[-1]+ f[-2])%m
        f.append(num)
    return f
r=fibo(n1)
print(r)

"""
Input : 5
Output : 0 1 1 2 3 5
🧾 Problem says:
We are given n, and we must return all Fibonacci numbers from 0th term to nth term.
We also must return numbers modulo 10⁹ + 7 (means we take the remainder after dividing by 1,000,000,007 — this just prevents very large numbers).
Input:
n = 5
Output:
0 1 1 2 3 5

🪄 Let’s Dry Run (Example: n = 5)
Input: n = 5
MOD = 10**9 + 7 → 1000000007

if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
n is not 0 or 1, so we skip this part :

Start list
f = [0, 1]
So currently, we have first two terms. f = [0, 1]

Start loop
We will run loop from i = 2 to i = 5.

💡 Why we use MOD = 10**9 + 7 in coding problems?
Because Fibonacci numbers (and many other series) grow very large very quickly.
Example: for f(100) the result will be : 354224848179261915075
* IT CAN OVERFLOW OR SLOW DOWN CALCULATION *

MOD = 10**9 + 7  (which is 1,000,000,007)
“If any number(which user will input) becomes bigger than 1,000,000,007, cut it down to its remainder after dividing by 1,000,000,007.”
Suppose user input n=100 so output will be 354224848179261915075. this output is soo large so it will cut down 354224848179261915075 % 1000000007 = 8745084. 
The result will get is : 8745084

🌀 Iteration 1 : (i = 2)
👉 Last two numbers: f[-1] = 1, f[-2] = 0
👉Add :num = (1 + 0) % MOD = 1
👉 Add to list: f = [0, 1, 1]

🌀 Iteration 2 : (i = 3)
👉 Last two numbers: f[-1] = 1, f[-2] = 1
👉 Add: num = (1 + 1) % MOD = 2
👉 Add to list: f = [0, 1, 1, 2]

🌀 Iteration 3 : (i = 4)
👉 Last two: f[-1] = 2, f[-2] = 1
👉 Add: num = (2 + 1) % MOD = 3
👉 Add to list: f = [0, 1, 1, 2, 3]

🌀 Iteration 4 (i = 5)
👉 Last two: f[-1] = 3, f[-2] = 2
👉 Add: num = (3 + 2) % MOD = 5
👉 Add to list: f = [0, 1, 1, 2, 3, 5]

✅ Step 5: Return answer
At the end, we have:   f = [0, 1, 1, 2, 3, 5]

"""

# Power Of Numbers
a = int(input("Enter the number: "))
r,m=0,a
while a>0:
    r=r*10 + a%10
    a=a//10
print(m**r)   # OR,   pow(m,r)

"""
Input: n = 2
Output: 4
Explanation: The reverse of 2 is 2, and 22 = 4.
Input: n = 10
Output: 10
Explanation: The reverse of 10 is 1 (leading zero is discarded), and 10 raised to the power 1 is 10.
"""








