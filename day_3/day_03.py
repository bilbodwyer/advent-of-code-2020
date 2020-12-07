#!/usr/bin/env python3

# Advent of Code
# Day 3
# bill@billodwyer.xyz

# Find the number of trees encountered while going down the mountain

map = []

with open("input", "r") as input:
    for line in input.readlines():
        map.append(line.strip())
    
height = len(map)
width = len(map[0])
    
def toboggan(x,y):
    trees = 0
    x_loc = 0
    y_loc = 0
    while y_loc < height:
        loc = map[y_loc][x_loc % width]
        if loc == "#":
            trees+=1
        x_loc+=x
        y_loc+=y
    return(trees)

        
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
trees = 1
for slope in slopes:    
    trees*=toboggan(slope[0],slope[1])

print(trees)
