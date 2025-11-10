#Day7 P34
#Leap year or not
y=int(input("Enter the year: "))
if((y%4==0) or (y%400==0) and (y%100 != 0)):
    print("Year is Leap Year")
else:
    print("Not a Leap year")
