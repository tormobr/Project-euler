
name_file = open("names.txt", "r")

names = sorted([name[1:-1] for line in name_file for name in line.split(",")])

print(sum([(i+1) * sum([ord(c)-64 for c in name]) for i, name in enumerate(names)]))
