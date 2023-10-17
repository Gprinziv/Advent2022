#bound the array by the difference between the left and right.
def main():
    with open("input") as f:
        walls = []
        for line in f.readlines():
            wall = [[int(x.split(",")[0]), int(x.split(",")[1])] for x in line.split(" -> ")]
            walls.append(wall)
    lmin = min(x[0] for wall in walls for x in wall)
    lmax = max(x[0] for wall in walls for x in wall)
    dmax = max(x[1] for wall in walls for x in wall)
    sandmap = [["0"] * (lmax-lmin+1) for _ in range(dmax+1)]
    
    sandmap[0][500-lmin] = "+"
    for wall in walls:
        last = wall.pop()
        sandmap[last[1]][last[0]-lmin] = "#"

        while len(wall) > 0:
            cur = wall.pop()
            if cur[1] == last[1]:
                steps = cur[0] - last[0]
                if steps > 0:
                    for i in range(1, steps+1):
                        sandmap[last[1]][last[0]-lmin + i] = "#"
                else:
                    for i in range(-1, steps-1, -1):
                        sandmap[last[1]][last[0]-lmin + i] = "#"
            else:
                steps = cur[1] - last[1]
                if steps > 0:
                    for j in range(1, steps+1):
                        sandmap[last[1] + j][last[0]-lmin] = "#"
                else:
                    for j in range(-1, steps-1, -1):
                        sandmap[last[1] + j][last[0]-lmin] = "#"
            sandmap[cur[1]][cur[0]-lmin] = "#"
            last = cur    

    #Now start dropping sand.
    sand = [500-lmin, 0]
    total = 0
    while True:
        try:
            if sandmap[sand[1] + 1][sand[0]] == "0":
                sand[1] += 1
            elif sandmap[sand[1] + 1][sand[0]-1] == "0":
                sand[0] -= 1
                sand[1] += 1
            elif sandmap[sand[1] + 1][sand[0]+1] == "0":
                sand[0] += 1
                sand[1] += 1
            else:
                sandmap[sand[1]][sand[0]] = "o"
                total += 1
                sand = [500-lmin, 1]
        except IndexError:
            print(sand)
            break
    
    #for line in sandmap:
    #    print(line)
    print(f"Total sand dropped: {total}")

def main2():
    with open("input") as f:
        walls = []
        for line in f.readlines():
            wall = [[int(x.split(",")[0]), int(x.split(",")[1])] for x in line.split(" -> ")]
            walls.append(wall)
    dmax = max(x[1] for wall in walls for x in wall) + 2
    sandmap = [["_"] * (dmax*2 + 1) for _ in range(dmax)] + [["#"] * (dmax*2+1
                                                                       )]
    
    sandmap[0][dmax] = "+"
    for wall in walls:
        last = wall.pop()
        sandmap[last[1]][dmax + last[0] - 500] = "#"

        while len(wall) > 0:
            cur = wall.pop()
            if cur[1] == last[1]:
                steps = cur[0] - last[0]
                if steps > 0:
                    for i in range(1, steps+1):
                        sandmap[last[1]][dmax + last[0] - 500 + i] = "#"
                else:
                    for i in range(-1, steps-1, -1):
                        sandmap[last[1]][dmax + last[0] - 500 + i] = "#"
            else:
                steps = cur[1] - last[1]
                if steps > 0:
                    for j in range(1, steps+1):
                        sandmap[last[1] + j][dmax + last[0] - 500] = "#"
                else:
                    for j in range(-1, steps-1, -1):
                        sandmap[last[1] + j][dmax + last[0] - 500] = "#"
            sandmap[cur[1]][dmax + cur[0] - 500] = "#"
            last = cur    

    #Now start dropping sand.
    sand = [dmax, 0]
    total = 0
    while sandmap[0][dmax] != "o":
        try:
            if sandmap[sand[1] + 1][sand[0]] == "_":
                sand[1] += 1
            elif sandmap[sand[1] + 1][sand[0]-1] == "_":
                sand[0] -= 1
                sand[1] += 1
            elif sandmap[sand[1] + 1][sand[0]+1] == "_":
                sand[0] += 1
                sand[1] += 1
            else:
                sandmap[sand[1]][sand[0]] = "o"
                total += 1
                #print(sand)
                sand = [dmax, 0]
                #for line in sandmap:
                #    print(line)
                #_ = input()
        except IndexError:
            print(f"Sand fell off the map at {sand}!")
            break
    
    #for line in sandmap:
    #    print(line)
    print(f"Total sand dropped: {total}")    

main()
main2()