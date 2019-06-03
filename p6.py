

# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025

# Hence the difference between the sum of the squares of the 

# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.


c = 0
a = 0
for i in range(101):
    a += i
    c += i*i
b = a*a

print(b - c)

