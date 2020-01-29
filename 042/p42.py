

def solve():
    words = open("words.txt").read().strip().split(",")
    res = []
    tris = create_tri(1000)
    for word in words:
        val = 0
        for c in word.upper():
            val += ord(c)-64
        if val in tris:
            res.append(word)
    return res, len(res)


def create_tri(n):
    ret = []
    for i in range(0,n):
        ret.append(int(0.5* (i * (i+1))))
    return ret


print(solve())
