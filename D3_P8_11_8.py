#Day3 P8
#Average of all the elements in the array
n=int(input("Enter the range: "))
a=list(map(int,input("Enter the values: ").split()))
s=0
for i in a:
    s=s+i
avg=s/n
print(int(avg))


"""
Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: 3
Explanation: Average is the sum of all the elements divided by number of elements.Therefore (1+2+3+4+5)/5 = 3.

"""