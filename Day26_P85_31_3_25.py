# Print all the duplicates in the string
a = input("Enter the String: ")
d={}
for i in a:
    b=a.count(i)
    if b>1:
        d[i]=b
if not d:
    print("No duplicate values")
else:
    for key,value in d.items():
        print(f"{key} - {value}")

"""
if not d:    check that if dictionary is empty or not, if empty means there is no duplicate value in the string 
that's why it's not store in dic
else print the dictionary in the mentioned output format

if not d:  
means we are checking is dic 'd' is empty or not. if empty == true it will print the above line "No Duplocate exist"
else it will move to the else part and print the dic

"""
# Example 1:
# Input:
#  str= "sinstriiintng"
# Output:
# i - 4
# n - 3
# s - 2
# t - 2
# Explanation:
# In the above example, 's' occurs twice, 'i' occurs four times, 't' occurs twice and 'n' occurs thrice. 'r' and 'g' occur only one time and hence are not considered.

# Example 2:
# Input:
#  str= "abcdefg"
# Output:
# < -- No Output -- >
# Explanation:

# In the above example, every character occurs only once(no duplicates), therefore nothing to print.