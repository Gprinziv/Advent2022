def p1():
    with open("input") as f:
        total = 0
        for line in f.readlines():
            first, second = line[:(len(line)//2)], line[(len(line)//2):-1]
            for letter in first:
                if letter in second:
                    total += ord(letter) - (38 if letter.isupper() else 96)
                    break
        return total


def p2():
    with open("input") as f:
        groups = [line.strip("\n") for line in f.readlines()]
    total = 0
    i = 0

    while i < len(groups):
        for letter in groups[i]:
            if letter in groups[i+1] and letter in groups[i+2]:
                total += ord(letter) - (38 if letter.isupper() else 96)
                break
        i += 3
    return total
    
print(p1())
print(p2())