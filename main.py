from re import split as resplit

def getStartingLists(start):
    start = start.split("\n")
    length = len(start[0]) + 1
    parsedList = []
    i = 0
    while i < length/4:
        temp = []
        for line in start[:-1]:
            if line[4*i + 1] != " ":
                temp.insert(0, line[4*i+1])
        parsedList.append(temp)
        i += 1
    return parsedList

def p1():
    with open("input") as f:
        start, moves = f.read().split("\n\n")
    
    instructions = []
    for line in moves.split("\n"):
        nums = [int(i) for i in resplit("[a-z ]+", line)[1:]]
        instructions.append(nums)
    boxes = getStartingLists(start)

    for amt, toBox, fromBox in instructions:
        boxes[fromBox-1] += reversed(boxes[toBox-1][-amt:])
        boxes[toBox-1] = boxes[toBox-1][:-amt]
    return "".join(i[-1] for i in boxes)

def p2():
    with open("input") as f:
        start, moves = f.read().split("\n\n")
    
    instructions = []
    for line in moves.split("\n"):
        nums = [int(i) for i in resplit("[a-z ]+", line)[1:]]
        instructions.append(nums)
    boxes = getStartingLists(start)

    for amt, toBox, fromBox in instructions:
        boxes[fromBox-1] += boxes[toBox-1][-amt:]
        boxes[toBox-1] = boxes[toBox-1][:-amt]
    return "".join(i[-1] for i in boxes)
    
print(p1())
print(p2())