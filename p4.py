

# A palindromic number reads the same both ways. 

#Find the largest palindrome made from the product of two 3-digit numbers.

prods = []
for i in range(100, 999, 1):
    for j in range(100, 999, 1):
        new = i*j
        if str(new) == str(new)[::-1]:
            prods.append(i*j)
print(max(prods))

# with list comprehensions
prods = [i*j for j in range(100,999,1) for i in range(100,999,1) if str(i*j) == str(i*j)[::-1]]
print(max(prods))


