

def get_digits(n):
    return len([c for c in str(n)])

current_fib = 1
last_fib = 1
index = 2
while get_digits(current_fib) < 1000:
    next_fib = current_fib + last_fib
    last_fib = current_fib
    current_fib = next_fib
    index += 1

print(index)
