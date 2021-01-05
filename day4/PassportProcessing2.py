import re

passports = open("input.txt", "r")

lines = []

for i in passports:
    if " " in i:
        j = i.split(" ")
        for k in j:
            lines.append(k.rstrip())
    else:
        lines.append(i.rstrip())        

temp = []
count = 0

eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

for i in lines:
    if i.split(":")[0] == "byr":
        if 1920 <= int(i.split(":")[-1]) <= 2002: 
            temp.append(i.split(":")[0])
    if i.split(":")[0] == "iyr":
        if 2010 <= int(i.split(":")[-1]) <= 2020: 
            temp.append(i.split(":")[0])
    if i.split(":")[0] == "eyr":
        if 2020 <= int(i.split(":")[-1]) <= 2030: 
            temp.append(i.split(":")[0])
    if i.split(":")[0] == "hgt":
        if "cm" in i:
            if 150 <= int(i.split(":")[-1].rstrip("cm")) <= 193:
                temp.append(i.split(":")[0])
        if "in" in i:
            if 59 <= int(i.split(":")[-1].rstrip("in")) <= 76:
                temp.append(i.split(":")[0])
    if i.split(":")[0] == "hcl":
        if i.split(":")[-1][0] == "#" and re.search("[0-9a-f]", i.split(":")[-1]) and len(i.split(":")[-1]) == 7:
            temp.append(i.split(":")[0])
    if i.split(":")[0] == "ecl":
        if i.split(":")[-1] in eyecolors:
            temp.append(i.split(":")[0])
    if i.split(":")[0] == "pid":
        if len(i.split(":")[-1]) == 9 and i.split(":")[-1].isnumeric():
            temp.append(i.split(":")[0])

    if i == "" or i is lines[-1]:   
        print(temp)
        if "byr" in temp and "iyr" in temp and "eyr" in temp and "hgt" in temp and "hcl" in temp and "ecl" in temp and "pid" in temp:
            count +=1
        temp = [] # clear the temporary list and start a new passport



print (count)