import time
import math

def solve(limit):
    match = "1234567890"
    for n in range(int(limit), 0, -1):
        if str(n**2)[::2] == match:
            return n
print(solve(math.sqrt(1929394959697989990)))
