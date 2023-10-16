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
        print(f"\nPair {i+1}\nLeft: {a}\nRight: {b}")
        
        
        
        
        
        
        
        
        
        
        """
        cur = 0
        while cur < len(a) and cur < len(b):
            print(f"\nPair {i+1}\nLeft: {a}\nRight: {b}")
            if type(a[cur]) == int and type(b[cur]) == int:
                if a[cur] < b[cur]:
                    total += i + 1
                    print("This one is good!")
                    break
                elif a[cur] > b[cur]:
                    print("This one is bad!")
                    break
                cur += 1

            #this doesn't work if there's more to do.    
            elif type(a[cur]) == list and type(b[cur]) == list:
                print("two lists!")
                a = a[cur]
                b = b[cur]
                cur = 0
            else:
                print("List and integer!")
                break
        if len(a) == 0 and len(b) > 0:
            total += i + 1
            print("This one is good!")
        elif len(b) == 0 and len(a) > 0:
            print("This one is bad!")"""

    print(f"Sum of indicies are {total}")
main()