def part1():
    with open("test") as f:
        cmds = [line.strip() for line in f.readlines()]

    dirs, i, cur = {}, 0, []

    while i < len(cmds):
        cmd = cmds[i].split()
        if cmd[1] =="cd":
            cur.pop() if cmd[2] == ".." else cur.append(cmd[2])
            i += 1
        elif cmd[1] == "ls":
            temp = [0]
            i += 1
            while i < len(cmds) and cmds[i][0] != "$":
                cmd = cmds[i].split()
                if cmd[0] == "dir":
                    temp.append(cmd[1])
                else:
                    temp[0] += int(cmd[0])
                i += 1
            dirs[cur[-1]] = temp

    print(dirs)
    #We've made our tree. Now how the hell do we solve for it efficiently?

part1()