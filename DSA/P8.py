# Printing a number pattern (1 / 1 2 / 1 2 3 …) for N rows

n=int(input("enter the range: "))
for i in range(n):
    for j in range(1,i+1):
        print(j,end=" ")
    print()