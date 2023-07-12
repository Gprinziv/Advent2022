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
    trees = array(getTrees("input"))
    t2 = rot90(trees,2)
    t3 = zeros((len(trees[0]), len(trees)), int)

    for j in range(1, len(trees)-1):
        lmax, rmax = trees[1][0], t2[1][0]
        umax, dmax = trees[0][:], t2[0][:]
        for i in range(1, len(trees[0])-1):
            if trees[j][i] > lmax:
                lmax = trees[j][i]
                t3[j][i] = 1
            if trees[j][i] > umax[i]:
                umax[i] = trees[j][i]
                t3[j][i] = 1
            if t2[j][i] > rmax:
                rmax = t2[j][i]
                t3[-1-j][-1-i] = 1
            if t2[j][i] > dmax[i]:
                dmax[i] = t2[j][i]
                t3[-1-j][-1-i] = 1
    return sum(sum(t3)) + 2 * (len(t3) + len(t3[0]) - 2)

def p2():
    trees = getTrees("input")
    total = len(trees) * len(trees[0])    
    return total
    
print(p1())
print(p2())