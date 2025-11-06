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
i start from 4(n-1) -> Print 4
Step -1: 4-1 = 3 -> print 3
Step -1: 3-1 = 2 -> print 2
Step -1: 2-1 = 1 -> print 1
Step -1: 1-1 = 0 -> print 0
step -1: 0-1 = -1 -> False Stop 
"""