# Arithmetic operators
a = 10
b = 3
print("a and b:", a, b)

print("a + b:", a + b)  # addition
print("a - b:", a - b)  # subtraction
print("a * b:", a * b)  # multiplication
print("a / b:", round(a / b, 3))  # division
print("a % b:", a % b)  # modulus
print("a // b:", a // b)  # floor division
print("a ** b:", a ** b, "\n")  # exponential

# Assignment operators
c = 5
print("c:", c)

c += 3  # add AND assignment
print("c += 3:", c)

c -= 3  # subtract AND assignment
print("c -= 3:", c)

c *= 3  # multiply AND assignment
print("c *= 3:", c)

c /= 3  # divide AND assignment
print("c /= 3:", c)

c %= 3  # mod AND assignment
print("c %= 3:", c)

c //= 3  # floor divide AND assignment
print("c //= 3:", c)

c **= 3  # exponential AND assignment
print("c **= 3:", c, "\n")

# Relational/comparison operators
d = 4
e = 8
print("d and e:", d, e)

print("d == e:", d == e)  # equal to
print("d != e:", d != e)  # not equal to
print("d > e:", d > e)  # greater than
print("d < e:", d < e)  # less than
print("d <= e:", d <= e)  # less than or equal to
print("d >= e:", d >= e, "\n")  # greater than or equal to

# Logical operators
f = True
g = False
print("f and g:", f, g)

print("f AND g:", f and g)  # logical AND
print("NOT f:", not f)  # logical NOT
print("NOT g:", not g)  # logical NOT
print("f OR g:", f or g)  # logical OR