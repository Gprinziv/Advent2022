with open("input") as f:
    instructions = [[x[0], int(x[2:].strip())] for x in f.readlines()]

def part1():
    head, tail = [0, 0], [0, 0]
    visited = set()
    visited.add(tuple(tail))

    for dir, val in instructions:
        if dir == "R": r, v, o = 1, 1, 0
        elif dir == "L": r, v, o = 1, -1, 0
        elif dir == "U": r, v, o = 0, -1, 1
        elif dir == "D": r, v, o = 0, 1, 1
        else: print("You goofed the input string.")

        for _ in range(val):
            head[r] += v
            if (v * head[r]) - (v * tail[r]) > 1:
                tail[r] += v
                if head[o] != tail[o]: tail[o] = head[o]
                visited.add(tuple(tail))
    print(len(visited))

def part2():
    knots = {}
    for i in range(10):
        knots[i] = [0,0]
    visited = set()
    visited.add(tuple(knots[9]))

    for dir, val in instructions:
        if dir == "R": r, v = 1, 1
        elif dir == "L": r, v = 1, -1
        elif dir == "U": r, v = 0, -1
        elif dir == "D": r, v = 0, 1
        else: print("You goofed the input string.")

        for _ in range(val):
            knots[0][r] += v
            for j in range(1, 10):
                if abs(knots[j-1][0] - knots[j][0]) > 1:
                    knots[j][0] += 1 if knots[j-1][0] > knots[j][0] else -1 
                    if knots[j-1][1] != knots[j][1]: knots[j][1] += 1 if knots[j-1][1] > knots[j][1] else -1

                elif abs(knots[j-1][1] - knots[j][1]) > 1:
                    knots[j][1] += 1 if knots[j-1][1] > knots[j][1] else -1
                    if knots[j-1][0] != knots[j][0]: knots[j][0] += 1 if knots[j-1][0] > knots[j][0] else -1

            visited.add(tuple(knots[9]))
    print(len(visited))

part1()
part2()