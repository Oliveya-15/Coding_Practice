n=int(input("Enter the Range: "))
a=list(map(int,input("Enter the numbers: ").split()))

#Using Reverse Function :-
#a.reverse()

#Using Slicing Method :-
#r = a[::-1]

r = []
for i in range(n-1, -1, -1):  
    r.append(a[i])
print("Reversed Array:", r)
