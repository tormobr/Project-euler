import math

# im not proud of this code

def solve():
    prod = [1,1]
    for i in range(11,100, 1):
        for j in range(i+1, 100, 1):
            if i % 10 == 0 or j % 10 == 0:
                continue
            if str(i)[0] == str(i)[1] or str(j)[0] == str(j)[1]:
                continue
            k,l = remove(i,j, 1)
            if i / j == k / l:
                prod[0] *= i
                prod[1] *= j
    return prod[1] /math.gcd(*prod)

def remove(i, j, index):
    i = str(i)
    to_remove = i[index]
    i = i[:index] + i[index+1:]
    j = str(j).replace(to_remove, "")
    print("to replace", to_remove)
    print("i: ", i, "j: ",j)
    return (int(i), int(j))  
    
res = solve()
print(res)
