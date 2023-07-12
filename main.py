class Monkey:
    def __init__(self, text):
        self.inspections = 0
        lines = text.split("\n")
        self.number = int(lines[0][7])
        self.items = [int(x) for x in lines[1].split(": ")[1].split(", ")]
        self.operation = lines[2].split("= ")[1]
        self.divisibility = int(lines[3].split()[-1])
        self.targets = [int(lines[4][-1]), int(lines[5][-1])]

    def evalItems(self, mList):
        for old in self.items:
            self.inspections += 1
            old = (eval(self.operation)) #// 3
            if old % self.divisibility == 0:
                mList[self.targets[0]].catch(old)
            else:
                mList[self.targets[1]].catch(old)
        self.items = []

    def getInspections(self):
        return self.inspections

    def catch(self, item):
        self.items.append(item)

    def getID(self):
        return self.number

    def getItems(self):
        return self.items

    def getOp(self):
        return self.operation

    def getDivisibility(self):
        return self.divisibility

    def getTargets(self):
        return self.targets

def part1():
    with open("input") as f:
        monkeylist = []
        for m in f.read().split("\n\n"):
            monkeylist.append(Monkey(m))

    for _ in range(10000):
        for monkey in monkeylist:
            monkey.evalItems(monkeylist)

    for monkey in monkeylist:
        print(f"Monkey items: {monkey.getItems()}. Number of inspections: {monkey.getInspections()}")
    iList = sorted([m.getInspections() for m in monkeylist])
    print(iList)
    print(iList[-1] * iList[-2])

part1()