#Check if given year is a leap year or not
y=int(input("Enter the Year: "))
if ((y%4 == 0 and y%100 != 0) or (y%400 == 0)):
    print("The Year is Leap Year")
else:
    print("The Year is not Leap Year")

#Input: 1996
# Output: Yes
# Explanation: Since 1996 is a leap year answer is “Yes”.