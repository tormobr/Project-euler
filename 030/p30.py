

def eval(upper):
    numbers = []
    for i in range(2, upper):
        if sum([int(x)**5 for x in str(i)]) == i:
            numbers.append(i)
    print(sum(numbers)) 

# some math calculations to get this upper boundary
upper = 6*9**5
eval(upper)
    
