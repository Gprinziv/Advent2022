from re import split as resplit

def p1():
    with open("input") as f:
        total = 0
        for line in f.readlines():
            a,b,c,d = [int(i) for i in resplit("[,-]", line.strip())]
            total += ((a<=c and b>=d) or (c<=a and d>=b))
    return total

def p2():
    with open("input") as f:
        total = 0
        for line in f.readlines():
            a,b,c,d = [int(i) for i in resplit("[,-]", line.strip())]
            total += (c<=b and d>=a)
    return total
    
print(p1())
print(p2())