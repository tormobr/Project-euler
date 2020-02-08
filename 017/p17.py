import sys

ones = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three", 
    4: "four", 
    5: "five", 
    6: "six", 
    7: "seven", 
    8: "eight", 
    9: "nine"
}

hax = {
    10: "ten", 
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen", 
    17: "seventeen", 
    18: "eighteen",
    19: "nineteen",

}
tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy", 
    8: "eighty", 
    9: "ninety",

}

hundreds = "hundred"

def solve():
    ret = ""
    for i in range(1, 1000):
        ret += print_num(i)
    return len(ret + "onethousand")

def print_num(n):
    ret = ""
    while n != 0:
        if "zero" in ret:
            print("this is shit")
            sys.exit(0)
        if n < 10:
            ret += ones[n] 
            n = 0
        elif n < 20:
            ret += hax[n]
            n = 0
        elif n < 100:
            ret += tens[n//10]
            n %= 10
        elif n < 1000:
            ret += ones[n//100] + hundreds
            n %= 100
            if n != 0:
                ret += "and"

    return ret

num = print_num(100)
print(len(num), num)
print(solve())
