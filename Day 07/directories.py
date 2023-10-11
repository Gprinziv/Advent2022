def main():
    with open("input") as f:
        cmds = [line.strip() for line in f.readlines()]

    dirs, dirCounter, i, cur = {}, 0, 0, []

    while i < len(cmds):
        cmd = cmds[i].split()
        if cmd[1] =="cd":
            if cmd[2] == "..":
                cur.pop()
            else:
                cur.append(dirCounter)
                dirs[dirCounter] = 0
                dirCounter += 1
            i += 1
        else:
            i += 1
            while i < len(cmds) and cmds[i][0] != "$":
                cmd = cmds[i].split()
                if cmd[0] != "dir":
                    for dir in cur:
                        dirs[dir] += int(cmd[0])
                i += 1
    print(dirs)    

    #Part 1
    total = sum([val for val in dirs.values() if val <= 100000])
    print(f"Sum of directories under 100k is {total}.")

    #Part 2
    needed = dirs[0] - 40000000
    print(f"The size of the smallest directory you can delete is {sorted([val for val in dirs.values() if val >= needed])[0]}")


main()