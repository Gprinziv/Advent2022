def p1():
    with open("input") as f:
        hands = [tuple(line.strip("\n").split(" ")) for line in f.readlines()]

    scores = {("A", "X"):4,("A", "Y"):8,("A", "Z"):3, \
              ("B", "X"):1,("B", "Y"):5,("B", "Z"):9, \
              ("C", "X"):7,("C", "Y"):2,("C", "Z"):6}
    total = sum(scores[i] for i in hands)
    return total


def p2():
    with open("input") as f:
        hands = [tuple(line.strip("\n").split(" ")) for line in f.readlines()]

    scores = {("A", "X"):3,("A", "Y"):4,("A", "Z"):8, \
              ("B", "X"):1,("B", "Y"):5,("B", "Z"):9, \
              ("C", "X"):2,("C", "Y"):6,("C", "Z"):7}
    total = sum(scores[i] for i in hands)
    return total
    
print(p1())
print(p2())