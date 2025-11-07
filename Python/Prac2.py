# Loop Statements :-

# For Loop : Printing Multiplication table
num=int(input("Enter the number: "))
for i in range(1,11):
    print(i*num)

"""Input: n = 6
Output: 6 12 18 24 30 36 42 48 54 60
"""

# Range usage using (STEP) skipping elements
s=input("Enter anything: ")
for i in range(0,len(s),2):
        print(s[i])

"""Input: s = "DoctorPhenomenal"
Output: DcoPeoea
"""

# While Loop :-
x=int(input("Enter the number: "))
while (x >= 0):
        print(x,end=" ")
        x -= 1
"""Input: x = 3
Output: 3 2 1 0
                  Initialization
x = 0                 Syntax : while condition :
while x < 9:                           Statements
  print(x)                             .....
  x = x + 1                      increement/decrement
"""

# Zero Converter :-
n=int(input("Enter the number: "))
if n==0:
        print("already Zero")
elif n>0:
        for j in range(n-1,-1,-1):
                print(j,end=" ")
elif n<0:
        for i in range(n,1):
                print(i,end=" ")
else:
        print("Something Worng")
"""Input: n = 0           Input:n = 4           Input:n = -3
Output:already Zero       Output:3 2 1 0        Output:-3 -2 -1 0
for i in range(n-1, -1, -1 )     :     Suppose n = 5
                                       Start(n-1) => 5-1=4 the loop starts from 4
                                       Stop(-1)   => The loop stops before it reaches number 0. to stop priting the end(stop) condition should be -1.   
                                       Step(-1)   => Decreases each  step backward
i start from 5(n-1) -> Print 4
Step -1: 4-1 = 3 -> print 3
Step -1: 3-1 = 2 -> print 2
Step -1: 2-1 = 1 -> print 1
Step -1: 1-1 = 0 -> print 0
step -1: 0-1 = -1 -> False Stop 
"""

# Case Match Conditioning Statement :-

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
o=int(input("Enter the Operator: "))
match o:
            case 1:
                print(a+b,end="")
            case 2:
                print(a-b,end="")
            case 3:
                print(a*b,end="")
            case _:
                print("Invalid",end="")

#Input: a = 1, b = 2, operator = 3
#Output: 2
#Explanation: 1 * 2 = 2


"""# Python Conditional Statement and Loops Coding Problem
1=>   The FizzBuzz Program
def fb(a):
    if a%3==0 and a%5==0:
        print("FizzBuzz")
    elif a%5==0:
        print("Buzz")
    elif a%3==0:
        print("Fizz")
    else:
        print(a)
a=int(input())
fb(a)

Input: a = 3    a = 5      a = 30 
Output: Fizz    Bizz       Fizzbuzz      else print the number



2=>   Even Odd Game
'Given a number n, number of apples in a bag. You and your friend are picking one apple turnwise from the bag. It is given that the first attempt is always by you. The person picking the last apple will be the winner. 

If you will win: print "You" (without quotes)
If your friend will win: print "Friend" (without quotes)'
n=int(input())
if n%2==0:
    print("Friend")
else:
    print("You")

Input: n = 9     n = 4
Output: You      Friend



3=>   Greatest of Three
a=int(input())
b=int(input())
c=int(input())
if (a>c and a>b):
    print(a)
elif (b>c and b>a):
    print(b)
else:
    print(c)

Input: a = 1, b = 2, c = 3
Output: 3
Explanation: Clearly, c = 3 is the greatest of (1, 2, 3)


4=>   Leap Year
year=int(input())
if ((year % 4==0 and year % 100!=0) or year % 400==0):
    print("True")
else:
    print("False")

Input: year = 2020
Output: True
Explanation: 2020 is leap year as it multilpe of 4 but not a multiple of 100.
"""
