# Convert Binary to Octal
n=input("enter the binary number: ")
b=int(n,2)
o=oct(b)[2:]
print(o)

"""
oct() function in Python converts a decimal number (base 10) into an octal number (base 8).
syntax: oct(number)   - Returns a string that starts with '0o' (which indicates it is in octal format).  =>  [0o146]
to remove '0o'  use this statement -  oct(decimal_number)[2:]   

102 - in decimal, 146 - in octal, 1100110 - in binary

n=1100110
001 100 110
001₂ → 1₈
100₂ → 4₈
110₂ → 6₈

Dry Run :-
n = 1100110 (string)
b = 1100110 => 102 (binary value convert into decimal)
o = 102 => 0o146 (decimal value convert into octal) [2:] (removed '0o' using slicing by removing first 2 element)

"""
# Example 1:.
# Input: N = 1100110
# Output: 146
# Explanation: 1100110 when converted to octal number is “146”.

# Example 2:
# Input: 11111
# Output: 37
# Explanation: 11111 when converted to octal number is “37”.