#Day4 P12
#Adding Element in an array
a=list(map(int,input("Enter the values: ").split()))
n=int(input("Enter the value want to insert: "))
p=int(input("enter the Position want to enter(for beginning press 0, for end press 1,press 2 for specific position): "))
if p==1:
    a.append(n)
elif p==0:
    a.insert(0,n)
elif p==2:
    p1=int(input("Enter the position: "))
    a.insert(p1,n) 
else:
    print("Somthing went wrong: ")
print(a)


"""
Example:
Input: N = 5, array[] = {1,2,3,4,5}
insertbeginning(6)
insertending(7)
insertatpos(8,4)
Output: 6,1,2,8,3,4,5,7
Explanation: 6 is added at the beginning and 7 is added at the end and 8 is added at position 4 
"""