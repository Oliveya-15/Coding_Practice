# Check if given year is a leap year or not
y = int(input("Enter the year: "))
if (y%400 == 0) or ((y%4 == 0) and (y%100 != 0)):
    print("Year is Leap Year")
else:
    print("Year is not Leap Year")