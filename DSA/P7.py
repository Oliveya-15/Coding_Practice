# centered pyramid of stars for N rows

n=int(input("Enter the range: "))
for i in range(n):
    for j in range(n-1-i):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()

""" 
Output : 
      * 
    * * * 
  * * * * * 
* * * * * * * 
"""