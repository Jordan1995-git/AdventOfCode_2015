import numpy as np
import re

# open instructions
file = open('day6_input.txt')
instructions = file.readlines()
file.close

# Step 1: Create a grid of lights, all of which are switched off (set to value 0);
# for debugging start with a 4 by 4 grid with random numbers to see which cells change
# this is a 2D numpy array, much quicker to iterate through than a pandas dataframe
lights = np.zeros((1000,1000))
print(lights)
#indexing numpy 2D arrays works same as a data frame!
# 1000 is out of bounds, so 999 is the highes tnumber in an array of lenght 1000
# instructions = ["turn on 0,0 through 9,9", "turn off 1,5 through 4,7", "toggle 0,9 thruogh 4,9", "toggle 4,9 through 6,9"]
# Step 2: Get coordinates from instructions
for instruction in instructions:
    coords = re.findall(r"\b\d+\b", instruction)
    x1 = int(coords[0])
    y1 = int(coords[1])
    x2 = int(coords[2])+1 #+1 needed because of pythonic indexing
    y2 = int(coords[3])+1
# Step 3: Decide whether to turn on, turn off, or toggle the lights at these coordinates   
    if "turn on" in instruction:
        lights[x1:x2, y1:y2] = 1 #turn on all lights in the range

    elif "turn off" in instruction:
        lights[x1:x2, y1:y2] = 0 #turn off all lights in the range
    #if neither turning on or off, then toggle
    else:
        for row in range(x1, x2):# for each row within the coordinates
#             print(row)
            for col in range(y1, y2):  # check the value for each column
#                 print(lights_grid.iloc[row, col]) #this iterates through the whole range, so should work
                if lights[row, col] == 0:  # if it is 0, toggle it to 1
                    lights[row, col] = 1
#                     print(lights)
                else:  # otherwise, if it is 1 toggle it to 0
                    lights[row, col] = 0
#                     print(lights)

print(lights)
print(lights.sum())
# answer: 400410 lights on at the end
