#Find Sum of AP Series
#AP series formula :- sum_ap = (n / 2) * (2 * a + (n - 1) * d)
n = int(input("Enter the number: "))
d = int(input("Enter the d value: "))
a = int(input("Enter value of a: "))
s = (n/2)*(2*a+(n-1)*d)
print(s)