# Calculate Frequency of characters in a String
a = input("Enter the String: ")
f={}
for i in a:
    b=a.count(i)
    f[i]=b
for key,value in f.items():
    print(f"{key}{value} ",end="")

"""
For appending value-key as pair in any dictionary syntax is: dic[key] = value
example - f[i] = b    where i hold key and b hold values
=> {'m': 2, 'y': 1, ' ': 3, 'n': 1, 'a': 1, 'e': 1, 'i': 3}   here, m,y,n,a,e,i hold by i(key). 2,1,3,1,1,1,3 are hold by b(values)

By-default dic prints like this:   {'m': 2, 'y': 1, ' ': 3, 'n': 1, 'a': 1, 'e': 1, 'i': 3}    if we don't want to print like this
want to remove { } and commas, if we want to print like this : m2 y1  3 n1 a1e1 i3   then we need to write:
for key, value in f.items():
    print(f"{key}{value}", end=" ")

f.items() → Gives key-value pairs from the dictionary.   
for key, value in f.items() → Loops through each character (key) and its count (value).
print(f"{key}{value}", end=" ") → Prints each key-value pair without brackets and commas.
"""


# Example 1:
# Input: takeuforward
# Output: a2 d1 e1 f1 k1 o1 r2 t1 u1 w1 
# Explanation: Count of every character of string is printed.

# Example 2:
# Input: articles
# Output: a1 c1 e1 i1 l1 r1 s1 t1 
# Explanation: Count of every character of string is printed.