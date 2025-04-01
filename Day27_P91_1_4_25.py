# Find word with highest number of repeated letters in string
a = input("Enter the string: ")
b = a.split()
s = ""
r = 1
for i in b:
    h = 1
    for j in i:
        c = i.count(j)
        if c > h :
            h = c
    if h > r:
        r = h
        s = i
if r == 1:
    print("-1")
else:
    print(s)


# Example 1:
# Input: string=”abcdefghij google microsoft”
# Output: google
# Explanation: In “google” g appears 2 times, o appears 2 times which is highest among all words

# Example 2:
# Input: string = “cameron blue”
# Output: -1
# Explanation: No word has more than 1 letter.
