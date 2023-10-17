import re
TEST = 10
TEST2 = 21
PART1 = 2000000
PART2 = 4000001


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

#Find the sdiff of each beacon, then in a nested for loop compare the distance to each beacon to that of the point.
#Pros: Easy as hell to write.
#Cons: Slow, slow as shit. Like multiple days to finish slow
def main2():
    with open("test") as f:
        coords = []
        for line in f.readlines():
            coords.append([int(y) for y in re.split(",|:|=", line)[1::2]])
    #I could probably have done this in the above equation but meh, this works.
    #Get the sdiff for each beacon here.
    for x in range(len(coords)):
        coords[x] = coords[x] + [abs(coords[x][0] - coords[x][2]) + abs(coords[x][1] - coords[x][3])]
    
    """
    for j in range(PART2):
        for i in range(PART2):
            isoFlag = True
            for sen in coords:
                if (abs(sen[0] - i) + abs(sen[1] - j)) <= sen[4]:
                    isoFlag = False
                    break
            if isoFlag == True:
                print(f"Good coords at ({i}, {j})")
                return
    """
    for sen in coords:
        print(f"Coords ({sen[0]}, {sen[1]}); sdiff: {sen[4]}")
        for j in range(sen[1] - sen[4], sen[1] + sen[4] + 1):
            i = sen[4] - (j-sen[1]) 
            print(j)
        #check every point on the perimeter and compare it to the distances of each other beacon.
        #Start at the top, then go down-right, then go down-left, then go up-left, then go up-right.
#Let's look at it another way. WE don't need to check every point, just the points that are 1 greater than the perimeter of each beacon.


#main()
main2()