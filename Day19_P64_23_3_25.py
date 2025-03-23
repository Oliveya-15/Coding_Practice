# Convert digits/numbers to words
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

num = int(input("Enter a number: "))

words=""

if num==0:
    words="Zero"
if num>=1000:
    words+=ones[num//1000] + " thousand "
    num%=1000
if num>=100:
    words+=ones[num//100] + " hundred "
    num%=100
if num>=20:
    words+=tens[num//10] + " "
    num%=10
elif num>=10:
    words+=teens[num-10] + " "
    num=0
elif num>0:
    words+=ones[num] + " "

print("Output:    ", words.strip())

"""
🔹 Understanding This Part:
if num >= 1000:
    words += ones[num // 1000] + " thousand "
    num %= 1000  # Remove thousands place

    num = 7824
Check if num is 1000 or more:
7824 >= 1000, so this block runs.
Find the thousands place:
num // 1000 → 7824 // 1000 = 7
This gives 7, which is in the ones list:
    ones = ["", "one", "two", "three", ..., "seven", ...] => ones[7] = "seven"
Add "seven thousand" to words:
    words += "seven thousand "
Remove the thousands place from num:
    num %= 1000  # 7824 % 1000 = 824

    7824 % 1000 keeps only the last 3 digits (824).
Now num = 824, and we continue processing hundreds, tens, and on






Understanding This Part of the Code :-
if num >= 20:
    words += tens[num // 10] + " "
    num %= 10  # Remove tens place
🔹 Why Special Handling for num >= 20?
Unlike 10-19, where each number has a unique name (ten, eleven, twelve...), numbers 20 and above follow a pattern:
twenty-one, twenty-two, ..., twenty-nine
thirty-one, thirty-two, ..., thirty-nine...ninety-nine
These numbers always have two parts:
A tens word: twenty, thirty, forty, ... ninety + A ones word (if needed): one, two, three, ... nine
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
This list stores words for multiples of ten starting from 20 (index 2 in the list).

Example: num = 47
Let's go step by step to see what happens.
Step 1: Check Condition
num = 47
Condition: num >= 20 → ✅ (True)
The code inside this block will execute.
Step 2: Extract the Tens Place
num // 10 = 47 // 10 = 4
This gives 4, which corresponds to:
tens[4] = "forty"
Add "forty " to words:
words = "forty "
Step 3: Remove the Tens Place
num %= 10  # 47 % 10 = 7
This keeps only the ones digit (7).
Now num = 7, which will be processed in the next step (ones place handling).
words = "forty "
num = 7  # Ready for ones place processing





Understanding This Part of the Code :-
elif num >= 10:
    words += teens[num - 10] + " "
    num = 0  # No need to process ones place after this
Why Special Handling for 10-19?
Numbers from 10 to 19 have unique names that don't follow the usual pattern of "tens + ones."
For example:
10 → ten (not "one zero")
11 → eleven (not "one one")
12 → twelve (not "one two")
13 → thirteen, 14 → fourteen, etc.
Because they don’t follow the normal tens + ones structure, we need a special list to handle them.
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
         "sixteen", "seventeen", "eighteen", "nineteen"]
This list stores the words for numbers 10 to 19.
So, for example:
teens[0] = "ten"
teens[1] = "eleven"
teens[2] = "twelve"
teens[9] = "nineteen"

Example 1:    num = 13
num >= 10, so we enter this block.
num - 10 = 13 - 10 = 3, so we get:
    words += teens[3] + " "   =>  "thirteen"
Since we already converted the whole number, we set:
    num = 0  # No need to process ones place, This stops further processing.

Example 2:   num = 19
num >= 10, so this block runs.
num - 10 = 19 - 10 = 9, so:
words += teens[9] + " "   → "nineteen "
Again, no need to check ones place, so:
num = 0
The program stops.

🔹 Why num = 0?
After handling 10 to 19, there’s no separate ones place left.
Example:
"Thirteen" is just one word, no need to add an extra "three" after it.
If we didn’t set num = 0, it would keep processing and might mistakenly add "three" after "thirteen".

"""


# Input: 7824
# Output: seven thousand eight hundred twenty four
# Explanation: 7824 in words can be written as seven thousand eight hundred twenty four.

# Example 2:
# Input: 370
# Output: three hundred seventy
# Explanation: 370 in words can be written as three hundred seventy.