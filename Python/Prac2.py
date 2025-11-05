# Loop Statements :-

# For Loop : Printing Multiplication table
n=int(input("Enter the number: "))
for i in range(1,11):
    print(i*n)

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
