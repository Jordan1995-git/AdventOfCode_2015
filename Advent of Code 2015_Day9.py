import numpy as np
from itertools import permutations

file = "Day9_input.txt"
with open(file) as f:
    data = f.readlines()

start = []
end = []
distance = []

for line in data:
    line = line.strip()
    # first split input at the '=' and record the distance
    line = line.split(" = ")
    distance.append(int(line[1]))
    # then split at to and record the two destinations
    line = line[0].split(" to ")
    start.append(line[0])
    end.append(line[1])

# populate the data into a dictionary. each start and end location can be used as key, storing its matching start or end location
# and the distance between thm as a list like key[start] = [end, distance]
key = {}
for i in range(len(start)):
    key[start[i]] = [[end[i], distance[i]]]
# we can do this in one loop with try: except: but it was messing up my debugging in Thonny so I did it in 2 loops
for i in range(len(start)):
    if [end[i], distance[i]] not in key[start[i]]:
        key[start[i]].append([end[i], distance[i]])

# create a permutations list of all possible routes Santa could take
# first get all unique destinations in the start and end list
destinations = start + end
to_visit = np.unique(destinations)
# calculate permutations using the permutations function from itertools
perms = permutations(to_visit, len(to_visit))
# place all permutations in a list, these are all possible routes santa could take
all_routes = []
for p in perms:
    all_routes.append(list(p))

#initiate smallest as a very large number and largest as 0
smallest = 10000
largest = 0
# calculate the distance for each route - here is the hard part!
for route in all_routes:
    # initiate the distance for each route as 0
    dist = 0
    #     print(f"the route is {route}")
    # for each route
    for i in range(len(route) - 1):
        # if the first destination is defined in the dictionary
        if route[i] in key:
            #             print("if")
            # for every entry, which is in the form of a list of [destination, distance]
            found = 0 # keep track if the next stop in the route is in the definition for the current stop
            for dat in (key[route[i]]):
                #                 print(dat)
                # check if the destination of that entry is the second destination of the route
                if dat[0] == route[i + 1]:
                    # print()
                    # if it is, add the distance between the two destinations to the calculation
                    dist += dat[1]
                    found += 1 #

        # if the route is not in the dictionary key, check if the next one is
        # e.g. london-belfast is in the dictionary but not belfast-london.if we are going from
        # belfast to london, we would get the distance based on the london to belfast entry
        if route[i + 1] in key or found == 0:  #also run this if the current stop is defined, but the next stop is not part of its definition (has not been found)
            #             print("elif")
            for dat in (key[route[i + 1]]):
                #                 print(dat)
                # check if the destination of that entry is the first destination of the route
                if dat[0] == route[i]:
                    # print("True")
                    # if it is, add the distance between the two destinations to the calculation
                    dist += dat[1]
    # chrck if the current route distance is smaller than the smallest so far
    if dist < smallest:
        smallest = dist # if it is, replace the value of smallest with the current distance
    #check if the current distance is largert than the largest recorded so far
    if dist > largest:
        largest = dist #if it is record it as the largest

print(f"Part one answer: the shortest route distance is {smallest}")
print(f"Part two answer: the longest route distance is {largest}")