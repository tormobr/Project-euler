# the non sexy way
summ = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        summ += i
print(summ)

# the sexy way
print(sum([x for x in range(1000)if x % 3 == 0 or x % 5 == 0]))
