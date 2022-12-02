def p1():
    with open("input") as f:
        elves = f.read().split("\n\n")
    max = 0
    for elf in elves:
        total = sum(int(i) for i in elf.split("\n"))
        max = max if max > total else total
    return max

def p2():
    with open("input") as f:
        elves = f.read().split("\n\n")
    max = [0, 0, 0]
    for elf in elves:
        total = sum(int(i) for i in elf.split("\n"))
        max.append(total)
        max = sorted(max)[1:]
    return sum(max)

print(p1())
print(p2())