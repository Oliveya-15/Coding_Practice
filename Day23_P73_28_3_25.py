# Remove all vowels from the String
a = input("Enter the string: ")
l=["a","e","i","o","u","A","E","I","O","U"]
a=list(a)
for i in a:
    if i in l:
        a.remove(i)
print("".join(a))


"""
a=list(a)  converting a from string to list
coz, remove function can't be use on string. it's only appliable in list
print("".join(a)) - for printing the output as string. otherwise each character will print as list as i before convert a into list.
 
"""


# Example 1:
# Input: Str = “take u forward”
# Output: tk  frwrd
# Explanation: All vowels are removed from the given String.

# Example 2:
# Input: Str = “I am very happy today”
# Output:  m vry happy tdy
# Explanation: All vowels are removed from the given String.