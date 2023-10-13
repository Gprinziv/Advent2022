#If both are integers, the left (i) should be lower than the right (j).
#If they're the same, i+1 and j+1

#If both are lists, compare the value of each list as above.
#if the left list runs out first, correct.
#Right list ending first is incorrect.

#If one is n integer, convert it to a list and compare.
def goDeeper():
    pass

def main():
    with open("test") as f:
        signals = f.read().split("\n\n")
    total = 0

    for i in range(len(signals)):
        a, b = signals[i].split("\n")
        a, b = eval(a), eval(b)
        print(f"Pair {i+1}\nLeft: {a}\nRight: {b}\n")
        cur = 0
        while cur < len(a) and cur < len(b):
            if type(a[cur]) == int and type(b[cur]) == int:
                if a[cur] < b[cur]:
                    total += i + 1
                    print("This one is good!")
            

main()