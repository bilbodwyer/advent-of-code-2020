#!/usr/bin/env python

# Advent of Code
# Day 1
# bill@billodwyer.xyz

# Find the two entries in the list (input.csv) which sum to 2020 and then multiply them together
import time
startTime = time.time()
# Create empty list and import data into it as integers
expenses = []
with open("day_01_input.csv", "r") as input:
    for line in input.readlines():
        expenses.append(int(line))
        
# Set target number, length of input list, and starting index i
target = 2020
length = len(expenses)

# Two numbers summing to target
i = 0 
while i < length:
    for n in range(i+1, length):
        if expenses[i] + expenses[n] == target:
            print(expenses[i] * expenses[n])
    i+=1

# Three numbers summing to target
i = 0
while i < length:
    for n in range(i+1, length):
        for m in range(n+1,length):
            if expenses[i] + expenses[n] + expenses[m] == target:
                print(expenses[i] * expenses[n] * expenses[m])
    i+=1


executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
