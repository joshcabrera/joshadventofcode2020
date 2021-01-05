passports = open("input.txt", "r")

lines = []

# so here I wanted just a list of strings. Each passport
# will be separated in the list by a "" item in the list.

for i in passports:
    if " " in i:
        j = i.split(" ")
        for k in j:
            lines.append(k.rstrip())
    else:
        lines.append(i.rstrip())        

temp = []
count = 0

# we go through each item in the list and add it to our temporary list
# as long as it isn't a "" (because that would mark the end of a passport),
# taking out what's after the ":" because I want to use ("abc" in list) so
# we just want the abc alone

for i in lines:
    if i != "":
        temp.append(i.split(":")[0])
    if i == "" or i is lines[-1]:   # if we don't check if it's the last item, we'll be
                                    # off by one
        print(temp)
        if "byr" in temp and "iyr" in temp and "eyr" in temp and "hgt" in temp and "hcl" in temp and "ecl" in temp and "pid" in temp:
            count +=1
        temp = [] # clear the temporary list and start a new passport



print (count)