

def eval(l, h):
    res = []
    for i in range(l,h):
        for j in range(l,h):
            ans = i**j
            if ans not in res:
                res.append(ans)
    print(len(res))

eval(2,101)
    

