# Find all Symmetric Pairs in the array of pairs
n = int(input("Enter the range: "))
a = [list(map(int,input("Enter the numbers: ").split()[:2]))for i in range(n)]
s = []
for i in a:
    r = [i[1],i[0]]
    if r in a and r!=a and r not in s:
        s.append(i)
print(s)
