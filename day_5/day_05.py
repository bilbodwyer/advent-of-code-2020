#!/usr/bin/env python3

# Advent of Code
# Day 5
# bill@billodwyer.xyz

boarding_passes = []

with open("input","r") as input:
    boarding_passes = input.read().splitlines()
    
highest_seat_id = 0
seat_id_list = []

for string in boarding_passes:
    row = string[:-3]
    col = string[-3:]

    row_bin = row.replace("F", "0")
    row_bin = row_bin.replace("B", "1")
    col_bin = col.replace("L", "0")
    col_bin = col_bin.replace("R", "1")

    row_num = int(row_bin, 2)
    col_num = int(col_bin, 2)

    id_calc = (row_num * 8) + col_num
    if id_calc > highest_seat_id:
        highest_seat_id = id_calc
    seat_id_list.append(id_calc)


total_seats = len(seat_id_list)

for i in range(0,total_seats):
    if i not in seat_id_list:
        if i+1 in seat_id_list and i-1 in seat_id_list:
            your_seat = i
            
print(f"Highest seat ID is {highest_seat_id}")
print(f"Your seat ID is {your_seat}")
