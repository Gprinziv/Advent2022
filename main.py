import re
TEST = 10
PART1 = 2000000


def main():
    target = PART1
    empty = set()
    full = set()

    with open("input") as f:
        coords = []
        for line in f.readlines():
            coords.append([int(y) for y in re.split(",|:|=", line)[1::2]])


    #Calculate the "reach" of the coordinate by abs(dx) + abs(dy), then subtract the current y value from that sum. That is the range (plus and minus)
    #from x that can't have a beacon. Add those x values to a set, then count the length of the set minus the length of a second set of beacons
    #at y = target
    for sensor in coords:
        if sensor[3] == target:
            full.add(sensor[2])

        sdiff = abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])
        #print(f"Sensor: {sensor} has reach of {sdiff}")
        if sensor[1] > target:
            xrange = sdiff - (sensor[1] - target)
        else:
            xrange = sdiff + (sensor[1] - target)

        #print(f"Sensor has an xrange of {xrange}")
        if xrange >= 0:
            for i in range(sensor[0]-xrange, sensor[0]+xrange+1):
                empty.add(i)
        
    #print(f"The full set is {full}")
    #print(f"The empty set is {empty}")
    print(len(empty) - len(full))


def main2():
    with open("input") as f:
        pass

main()
main2()