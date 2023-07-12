with open("input") as f:
    instructions = [line.strip() for line in f.readlines()]

def part1():
    cycle = 0
    x = 1
    sum = 0

    for instruct in instructions:
        cycle += 1
        if cycle % 40 == 20 and cycle <= 220:
            sum += x * cycle

        if instruct == "noop": continue
        
        cycle += 1
        if cycle % 40 == 20 and cycle <= 220:
            sum += x * cycle

        x += int(instruct.split()[1])

    print(sum)

def part2():
    cycle, x = 0, 1
    lines = ""

    for instruct in instructions:
        char = "#" if abs(cycle % 40 - x) <= 1 else "."
        lines = "".join([lines, char])
        cycle += 1
        if cycle % 40 == 0: lines = "".join([lines, "\n"])
        if instruct == "noop": continue

        char = "#" if abs(cycle % 40 - x) <= 1 else "."
        lines = "".join([lines, char])
        cycle += 1
        if cycle % 40 == 0: lines = "".join([lines, "\n"])
        x += int(instruct.split()[1])
    print(lines)

part1()
part2()