import re
TEST, TEST2, PART1, PART2 = 10, 21, 2000000, 4000000

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
        coords = []
        for line in f.readlines():
            coords.append([int(y) for y in re.split(",|:|=", line)[1::2]])

    #I could probably have done this in the above equation but meh, this works.
    #Get the sdiff for each beacon here.
    for x in range(len(coords)):
        coords[x] = coords[x][0:2] + [abs(coords[x][0] - coords[x][2]) + abs(coords[x][1] - coords[x][3])]

    #So each beacon makes four lines. The positive lines are sen[1] - sen[0] +- (sdiff+1). The negative lines are sen[1] + sen[0] +- (sdiff+1)
    #Add all coefficients to a list.
    pos, neg = set(), set()
    for sen in coords:
        pos.add(sen[1] - sen[0] + sen[2] + 1)
        pos.add(sen[1] - sen[0] - sen[2] - 1)
        neg.add(sen[1] + sen[0] + sen[2] + 1)
        neg.add(sen[1] + sen[0] - sen[2] - 1)

    #x+pos = -x+neg => x+x = neg - pos => x = (neg-pos)/2
    #y = (neg-pos)/2 + pos => y = (neg - pos + 2pos)/2 => y = (pos+neg)/2
    #For each pos, neg pair, the intersection point is ((neg-pos)/2, (pos+neg)/2)
    for p in pos:
        for n in neg:
            intersect = (int((n-p)/2), int((n+p)/2))
            if all(0<=i<=PART2 for i in intersect):
                beaconFlag = True
                for sen in coords:
                    if abs(sen[0] - intersect[0]) + abs(sen[1] - intersect[1]) <= sen[2]:
                        beaconFlag = False
                if beaconFlag == True:
                    print(f"Found it at {intersect}")
                    print(f"Tuning frequency is {intersect[0] * PART2 + intersect[1]}")

#main()
main2()