import numpy as np
import re

# open instructions
file = open('day6_input.txt')
instructions = file.readlines()
file.close

# Step 1: Create a grid of lights, all of which are switched off (set to value 0);
# for debugging start with a 4 by 4 grid with random numbers to see which cells change
#this is a 2D numpy array, much quicker to iterate through than a pandas dataframe
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
        lights[x1:x2, y1:y2] += 1  #turn on increases intensity by 1
#         
    elif "turn off" in instruction: #turn off decreases it by 1 unless already 0
        for row in range(x1, x2):# for each row within the coordinates
            for col in range(y1, y2):  # and for each column cell 
                if lights[row, col] >0:  #if the intensity is > 0
                    lights[row, col] -= 1 #decrease it by 1
#   #if the option is toggle         
    else:
        lights[x1:x2, y1:y2] += 2 #increase the intensity by 2

print(lights) #get final array
print(lights.sum()) #and total final intensity
     
