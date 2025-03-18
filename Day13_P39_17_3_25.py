# Maximum and Minimum Digit in a Number
n = int(input("Enter the Number: "))
l = 0  # Set to 0 to track the largest digit correctly
s = 9  # Set to 9 to track the smallest digit correctly

while n > 0:
    r = n % 10  # Extract last digit
    l = max(l, r)  # Update max digit
    s = min(s, r)  # Update min digit
    n = n // 10  # Remove last digit

print(l, "Largest")
print(s, "Smallest")


"""     
Iteration	n (Remaining)	r = n % 10 (Extract Last Digit)      	max_digit	        min_digit	               n //= 10 (Remove Last Digit)
1st	       2746	                   6	                           max(0, 6) = 6	    min(9, 6) = 6	                  274
2nd	       274	                   4	                           max(6, 4) = 6	    min(6, 4) = 4	                  27
3rd	        27	                   7	                           max(6, 7) = 7	    min(4, 7) = 4	                   2
4th	        2	                   2	                           max(7, 2) = 7	    min(4, 2) = 2	                0 (Loop ends)

"""
    

# Input: N = 2746
# Output: Largest digit: 7
#         Smallest digit: 2
# Explanation: By simply going through the digits of 
# the number, we figure out the largest and smallest 
# digit in the number.
