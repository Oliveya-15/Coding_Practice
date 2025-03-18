#Find all Palindrome Numbers in given range
n=int(input("Enter the range: "))
a=list(map(int,input("Enter the numbers: ").split()))
f=[]
for i in a:
    s=0
    p=i
    while i>0:
        r=i%10
        s=(s*10)+r
        i=i//10
    if p==s:
        f.append(p)
print("Palindrome numbers are: \n")
print(f)

"""
i=121 n=3 [121,253,39]
121>0:
r=121%10 = 1
s=(0*10)+1 = 1
i=121//10 = 12

Countinue........this way each time check for each number

# Declare s=0, p=i inside for loop otherwise if you declare it inside while loop each time the value will update whioch we don't want
# if p==s: declare inside while bcz if we declare it outside the while loop then it can't understand the value which p hold 

"""

#input: n=4
# a = [121,342,565,781]
# output: [121,565]