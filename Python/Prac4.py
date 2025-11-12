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







