# Capitalize first and last character of each word of a string
a=input("enter the String: ")
r=[]
b=a.split()
for i in b:
    f=i[0].upper()
    m=i[1:-1]
    l=i[-1].upper()
    r.append(f+m+l)
print(" ".join(r))


        


# Example 1:
# Input: String str = "take u forward is awesome"
# Output: “TakE U ForwarD IS AwesomE”
# Explanation: We get the result after capitalizing the first and last character of each word of a string

# Example 2:
# Input: String str = "Take u Forward is Awesome"
# Output: “TakE U ForwarD IS AwesomE”
# Explanation: Characters T, F, A are initially in uppercase , so they remain as they are in the result.