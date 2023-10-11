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
    tmap = zeros((len(trees[0]), len(trees)), int)

    t2 = rot90(trees, -1)
    print(t2)
    for j in range(1, len(trees)-1):
        for i in range(1, len(trees[0])-1):
            if trees[j][i] > max(trees[j][:i]) or trees[j][i] > max(trees[j][i+1:]) or trees[j][i] > max(t2[i][-j:]) or trees[j][i] > max(t2[i][:-j-1]):
                tmap[j][i] = 1
                
    #The forest is a perfect square so we can "simplify" to the length of a side - 1
    return sum(sum(tmap)) + 4 * (len(tmap) - 1)

def p2():
    trees = getTrees("input")
    total = len(trees) * len(trees[0])    
    return total
    
print(p1())
print(p2())