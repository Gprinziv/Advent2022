def part1():
    with open("input") as f:
        cmds = [line.strip() for line in f.readlines()]

    dirs, i, cur = {}, 0, []

    while i < len(cmds):
        cmd = cmds[i].split()
        if cmd[1] =="cd":
            if cmd[2] == "..":
                cur.pop()
            else:
                cur.append(cmd[2])
                if cmd[2] not in dirs.keys():
                    dirs[cmd[2]] = 0
            i += 1
        elif cmd[1] == "ls":
            i += 1
            while i < len(cmds) and cmds[i][0] != "$":
                cmd = cmds[i].split()
                if cmd[0] != "dir":
                    for j in range(len(cur)):
                        dirs[cur[j]] += int(cmd[0])
                i += 1

    total = sum([val for val in dirs.values() if val < 100000])
    print(total)

part1()