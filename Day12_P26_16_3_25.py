#Check if a number is Prime or not
n=int(input("Enter the number: "))
c=0
for i in range(1,n+1):
    if n%i == 0:
        c=c+1
if c==2:
    print("The number is Prime: ",n)
else:
    print("The number is not Prime: ",n)

"""
for prime range should be always 1,n+1
bcz, the number is prime only when it devide with 1 & that number 
if we write like - range(0,n+1)  or  range(n)  or range(0,n)  or  range(n+1) whatever any of these does not satisfy the condition
bcz, only range(1,n+1) satisy as it start checking from 1 upto that number

n=7
i=1  1%7 == 0 done
i=2  2%7 != 0
i=3  3%7 != 0
i=4  4%7 != 0
i=5  5%7 != 0
i=6  6%7 != 0
i=7  7%7 == 0 done

7 is prime

""" 
#Input : 7
#Output: The number is Prime