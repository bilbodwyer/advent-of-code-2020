#!/usr/bin/env python

# Advent of Code
# Day 2
# bill@billodwyer.xyz

# Find the number of passwords in the list which are valid

import re

# Create empty list and import data
passwords = []
with open("input", "r") as input:
    for line in input.readlines():
        line = re.sub("\n","",line)     # strips newlines
        line = re.split(":\s|\s",line)  # convert to 3-part list: numbers, letters, password
        passwords.append(line)
        
# Part 1
# Set variable for final output
# valid_passwords = 0

# for password in passwords:
#     # find actual numbers in entry and create min and max allowed amounts
#     n = re.findall("\d{1,2}",password[0])
#     n_min = int(n[0])
#     n_max = int(n[1])
#     # set the letter as l
#     l = password[1]
#     # set the password as p
#     p = password[2]

#     #if l is in p, and number of l is within n_min/n_max, increase valid_passwords by 1
#     if l in p:
#         if p.count(l) >= n_min and p.count(l) <= n_max:
#             valid_passwords +=1

# print(valid_passwords)

# Part 2
Set variable for final output
valid_passwords = 0

for password in passwords:
    # find actual numbers in entry and create first and last positions
    n = re.findall("\d{1,2}",password[0])
    n_first = int(n[0]) - 1
    n_last = int(n[1]) - 1
    
    
    # set the letter as l
    l = password[1]
    
    # set the password as p
    p = password[2]
    
    if p[n_first] == l:
        if p[n_last] != l:
            valid_passwords +=1
    if p[n_first] != l:
        if p[n_last] == l:
            valid_passwords +=1


print(valid_passwords)
