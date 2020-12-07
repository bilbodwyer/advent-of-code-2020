#!/usr/bin/env python3

# Advent of Code
# Day 4
# bill@billodwyer.xyz

# Find the number of valid passports

import re

passports = []

with open("input", "r") as input:
    passport_dict = {}
    for line in input:
        if ":" in line:
            line = line.strip()
            line = re.split(" ",line)
            for entry in line:
                key,value = entry.split(":")
                passport_dict[key] = value
        else:
            passports.append(passport_dict)
            passport_dict = {}

def check_valid(passports):
    valid_passports = 0 
    for passport in passports:
        if len(passport.keys()) == 8:
            valid_passports += 1
        elif len(passport.keys()) == 7:
            if not any("cid" in key for key in passport):
                valid_passports += 1
    print(str(valid_passports) + " valid passports found")
    

def validate_year(passport,a,z,year):
    if a <= int(passport[year]) <= z:
        return True
            

def validate_hgt(passport):
    if len(passport["hgt"]) >= 4:
        unit = str(passport["hgt"][-2:])
        hgt = int(passport["hgt"][:-2])
        if unit == "cm" and (150 <= hgt <= 193):
            return True
        if unit == "in" and (59 <= hgt <= 76):
            return True
        
def validate_hcl(passport):
    valid_code = "^#[a-f|\d]{6}(\n|$)"
    if re.match(valid_code,passport["hcl"]):
        return True

def validate_ecl(passport):
    valid_colours = ["amb","blu","brn","gry","grn","hzl","oth"]
    if passport["ecl"] in valid_colours:
        return True
            
def validate_pid(passport):
    if re.match("^\d{9}(\n|$)",passport["pid"]):
        return True


def validate(passports):
    valid_passports = 0
    for passport in passports:
        keys = len(passport.keys())
        current_passport = True

        if (keys == 7 and "cid" not in passport) or keys == 8:
            if not validate_year(passport,1920,2002,"byr"):
                current_passport = False
            if not validate_year(passport,2010,2020,"iyr"):
                current_passport = False
            if not validate_year(passport,2020,2030,"eyr"):
                current_passport = False
            if not validate_hgt(passport):
                current_passport = False
            if not validate_hcl(passport):
                current_passport = False
            if not validate_ecl(passport):
                current_passport = False
            if not validate_pid(passport):
                current_passport = False

        if keys == 7:
            if "cid" in passport:
                current_passport = False

        if keys < 7:
            current_passport = False

        if current_passport:
            valid_passports += 1

    print(str(valid_passports) + " valid passports found")


check_valid(passports)
validate(passports)
