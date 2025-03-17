#Find Sum of AP Series
#AP series formula :- sum_ap = (n / 2) * (2 * a + (n - 1) * d)
n = int(input("Enter the value of n: "))
a = int(input("Enter the value of a: "))
d = int(input("Enter the value of d: "))
sum_ap = (n / 2) * (2 * a + (n - 1) * d)
print(sum_ap)


"""
n=8 means until 8th term we have to do addition
a= -2 where a is the first term or initial value
d=5 means each time with the result add d

Below is the formula of A.P
sum_ap = (n / 2) * (2 * a + (n - 1) * d)

"""


# Input:
# n = 8, a = -2, d = 5

# A.P. Sequence:

# First term = -2   a
# Second term = -2 + 5 = 3   
# Third term = 3 + 5 = 8     
# Fourth term = 8 + 5 = 13   
# Fifth term = 13 + 5 = 18
# Sixth term = 18 + 5 = 23
# Seventh term = 23 + 5 = 28
# Eighth term = 28 + 5 = 33
# Now, adding all these terms:
# OutPut :  -2 + 3 + 8 + 13 + 18 + 23 + 28 + 33 => 124