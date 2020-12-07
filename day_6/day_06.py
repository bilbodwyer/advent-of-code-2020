#!/usr/bin/env python3

# Advent of Code
# Day 6
# bill@billodwyer.xyz


with open("input","r") as input:
    responses = []
    group = []
    for line in input.read().splitlines():
        if line == "":
            group = "".join(group)
            group = "".join(set(group))
            responses.append(group)
            group = []
        else:
            group.append(line)

sum = 0
for num in responses:
    sum += len(num)
    
print(f"Total sum of unique responses across all groups: {sum}")

with open("input","r") as input:
    responses = []
    group = []
    for line in input.read().splitlines():
        if line == "":
            responses.append(group)
            group = []
        else:
            group.append(line)

sum = 0
for group in responses:
    for a in group[0]:
        total = 0
        for person in group:
            if person.count(a):
                total +=1
        if total == len(group):
            sum+=1

print(f"Total sum of shared responses across all groups: {sum}")
