

def eval(l, h):
    res = []
    for i in range(l,h):
        for j in range(l,h):
            ans = i**j
            if ans not in res:
                res.append(ans)
    print(len(res))

def eval_pretty(l,h):
    print(len(set([i**j for i in range(l,h) for j in range(l,h)])))

eval(2,101)
eval_pretty(2,101)
    

