#!/usr/bin/env python

# Advent of Code
# Day 1
# bill@billodwyer.xyz

# Find the two entries in the list (input.csv) which sum to 2020 and then multiply them together

# Create empty list and import data into it as integers
expenses = []
with open("input", "r") as input:
    for line in input.readlines():
        expenses.append(int(line))
        
# Set target number, length of input list, and starting index i
target = 2020
length = len(expenses)

# Part 1
i = 0 
while i < length:
    for n in range(i+1, length):
        if expenses[i] + expenses[n] == target:
            print(expenses[i] * expenses[n])
    i+=1

# Part 2
i = 0
while i < length:
    for n in range(i+1, length):
        for m in range(n+1,length):
            if expenses[i] + expenses[n] + expenses[m] == target:
                print(expenses[i] * expenses[n] * expenses[m])
    i+=1

