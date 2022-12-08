from re import split as resplit

def getStartingLists():
    with open("input") as f:
        start, moves = f.read().split("\n\n")
    
    instructions = []
    for line in moves.split("\n"):
        nums = [int(i) for i in resplit("[a-z ]+", line)[1:]]
        instructions.append(nums)

    boxes = []
    start = start.split("\n")
    for i in range(1, len(start[0]))[::4]:
        temp = []
        for line in start[:-1]:
            if line[i] != " ":
                temp.insert(0, line[i])
        boxes.append(temp)
    return instructions, boxes

def p1():
    instructions, boxes = getStartingLists()
    
    for amt, toBox, fromBox in instructions:
        boxes[fromBox-1] += reversed(boxes[toBox-1][-amt:])
        boxes[toBox-1] = boxes[toBox-1][:-amt]
    return "".join(i[-1] for i in boxes)

def p2():
    instructions, boxes = getStartingLists()

    for amt, toBox, fromBox in instructions:
        boxes[fromBox-1] += boxes[toBox-1][-amt:]
        boxes[toBox-1] = boxes[toBox-1][:-amt]
    return "".join(i[-1] for i in boxes)
    
print(p1())
print(p2())