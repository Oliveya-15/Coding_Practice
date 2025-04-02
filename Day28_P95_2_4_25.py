# Reverse Words in a String
a = input("Enter the sentence: ")
b=a.split()
r=reversed(b)
print(" ".join(r))


    
# Example 1:
# Input: s=”this is an amazing program”
# Output: “program amazing an is this”

# Example 2:
# Input: s=”This is decent”
# Output: “decent is This”