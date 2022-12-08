def allDifferent(substring):
    for char in substring:
        if substring.count(char) > 1:
            return False
    return True

def p1():
    with open("input") as f:
        buffer, itr = f.read(), 3

        while itr < len(buffer):
            if allDifferent(buffer[itr-3:itr+1]):
                return itr + 1
            itr += 1
        return -1

def p2():
    with open("input") as f:
        buffer, itr = f.read(), 13

        while itr < len(buffer):
            if allDifferent(buffer[itr-13:itr+1]):
                return itr + 1
            itr += 1
        return -1
    
print(p1())
print(p2())