# Convert Binary to Octal
n = input("Enter the binary number: ")
b = int(n,2)
o = oct(b)[2:]
print("The octal form is: ",o)