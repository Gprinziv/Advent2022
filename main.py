from numpy import zeros
from numpy import rot90
from numpy import array

def getTrees(fn):
    trees = []
    with open(fn) as f:
        for line in f.readlines():
            trees.append([int(i) for i in line.strip()])
    return trees


def p1():
    trees = array(getTrees("test"))
    t2 = rot90(trees,2)
    t3 = zeros((len(trees[0]), len(trees)), int)

    print(trees)
    print(t2)
    print(t3)
    total = len(trees) * len(trees[0])

    lmax, umax, rmax, dmax = trees[1][0], trees[0][1], t2[1][0], t2[0][1]
    print(f"Left {lmax}, Right: {rmax}, Up: {umax}, Down: {dmax}")

    for j in range(1, len(trees)-1):
        for i in range(1, len(trees[0])-1):
            break
    return total

def p2():
    trees = getTrees("input")
    total = len(trees) * len(trees[0])    
    return total
    
print(p1())
print(p2())