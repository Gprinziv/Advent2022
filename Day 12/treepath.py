def main():
    with open("input") as f:
        topography = [line.strip() for line in f.readlines()]

    for j in range(len(topography)):
        if "S" in topography[j]:
            print(f"({topography[j].index('S')+1}, {j+1})")
        if "E" in topography[j]:
            print(f"({topography[j].index('E')+1}, {j+1})")
                


main()