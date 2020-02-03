from itertools import permutations
from collections import OrderedDict
import time


"""
def solve():
    print(len(pent.keys()))
    return
    for a in tri.keys():
        for b in square.keys():
            #if not is_cycle([a,b]):
                #continue
            for c in pent.keys():
                #if not is_cycle([a,b,c]):
                    #continue
                for d in hexx.keys():
                    #if not is_cycle([a,b,c,d]):
                        #continue
                    for e in hept.keys():
                        #if not is_cycle([a,b,c,d,e]):
                            #continue
                        for f in octt.keys():
                            items = [a,b,c,d,e,f]
                            print(items)
                            if is_cycle(items) and not same(items):
                                if True:
                                    print("found some good shit!!")
                                    time.sleep(100)

"""





def same(a):
    ret = set([f[n] for (f, n) in zip(funcs, a)])
    return len(ret) != len(a)



def is_cycle(a):
    perms = permutations(a)
    for p in perms:
        n = len(p)
        for i in range(len(a)-1):
            if str(p[i])[2:] != str(p[(i+1)])[:2]:
                break
        else:
            return True
    return False


def gen_tri(s, e):
    ret = OrderedDict()
    for i in range(1,e):
        num = int(i*(i+1)/2)
        if num > 9999:
            return ret
        if num > 1000:
            ret[num] = i

def gen_sq(s,e):
    ret = OrderedDict()
    for i in range(1,e):
        num = int(i**2)
        if num > 9999:
            return ret
        if num > 1000:
            ret[num] = i
def gen_pent(s,e):
    ret = OrderedDict()
    for i in range(1,e):
        num = int(i*((3*i)-1)/2)
        if num > 9999:
            return ret
        if num > 1000:
            ret[num] = i
def gen_hex(s,e):
    ret = OrderedDict()
    for i in range(1,e):
        num = int(i*((2*i)-1))
        if num > 9999:
            return ret
        if num > 1000:
            ret[num] = i
def gen_hept(s,e):
    ret = OrderedDict()
    for i in range(1,e):
        num = int(i*((5*i)-3)/2)
        if num > 9999:
            return ret
        if num > 1000:
            ret[num] = i
def gen_oct(s,e):
    ret = OrderedDict()
    for i in range(1,e):
        num = int(i*((3*i)-2))
        if num > 9999:
            return ret
        if num > 1000:
            ret[num] = i
    return  {i*((3*i)-2):i for i in range(s,e)}

e = 100000
s = 1000
tri = gen_tri(s,e)
square = gen_sq(s,e)
pent = gen_pent(s,e)
hexx = gen_hex(s,e)
hept = gen_hept(s,e)
octt = gen_oct(s,e)
funcs = [tri, square, pent, hexx, hept, octt]

print(solve())
