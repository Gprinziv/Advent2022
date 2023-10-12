from numpy import zeros
from numpy import rot90
from numpy import array
import math

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
    for j in range(1, len(trees)-1):
        for i in range(1, len(trees[0])-1):
            if trees[j][i] > max(trees[j][:i]) or trees[j][i] > max(trees[j][i+1:]) or trees[j][i] > max(t2[i][-j:]) or trees[j][i] > max(t2[i][:-j-1]):
                tmap[j][i] = 1
                
    #The forest is a perfect square so we can "simplify" to the length of a side - 1
    return sum(sum(tmap)) + 4 * (len(tmap) - 1)

def p2():
    trees = array(getTrees("input"))
    maxVis = 0   
    for j in range(1, len(trees)-1):
        for i in range(1, len(trees[0])-1):
            treeVis = [0, 0, 0, 0]
            
            for n in range(j-1, -1, -1):
                treeVis[0] += 1
                if trees[n][i] >= trees[j][i]:
                    break

            for n in range(j+1, len(trees)):
                treeVis[1] += 1
                if trees[n][i] >= trees[j][i]:
                    break

            for n in range(i-1, -1, -1):
                treeVis[2] += 1
                if trees[j][n] >= trees[j][i]:
                    break

            for n in range(i+1, len(trees[j])):
                treeVis[3] += 1
                if trees[j][n] >= trees[j][i]:
                    break

            visScore = math.prod(treeVis)
            if visScore > maxVis:
                maxVis = visScore
                print(f"Array ({i+1},{j+1}): {treeVis}; product: {visScore}")

    return maxVis
    
print(p1())
print(p2())