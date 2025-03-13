#Sort Elements of an Array by Frequency

n=int(input("Enter the range: "))
a=list(map(int,input("Enter the numbers: ").split()))
f=[]
for i in a:
    r=a.count(i)
    if i not in f:
        for _ in range(r):
            f.append(i) 
f.sort()
print(f)

"""
{1,2,3,2,4,3,1,2}
for i in a:
i=1
r=a.count(i)
r=2
if 1 is not in f:
then check how many times 1 is present in the array => 1 present 2(r) times. so add :-
this loop will add i(1) in f for r(2) times
now f = 1 1
continue........

"""
# Input: N = 8, array[] = {1,2,3,2,4,3,1,2}
# Output: 2 2 2 1 1 3 3 4 
# Explanation: Since  2 is present 3 times in an array , so print it 3 times ,then print ‘1’ 2 times and then ‘3’ 2 times and 4 has least frequency, it will be printed at last.