

def solve():
    return read_file("poker.txt")

def read_file(file_name):
    for line in open(file_name):
        if line:
            line = line.split()
            print(line)
    return ret

print(solve())
