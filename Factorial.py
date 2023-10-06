n = int(input("Enter the value of n: "))
new = 1

for i in range(1, n+1):
    new = new * i

print("Factorial of", n, "is:", new)