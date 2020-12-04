text = open("input.txt", "r")

trees_hit1 = 0
trees_hit2 = 0
trees_hit3 = 0
trees_hit4 = 0
trees_hit5 = 0

row = []
x = 0
y = 0

for i in text:
    row.append(i.rstrip())

#trees_hit1
while y < len(row)-1:
    y += 1

    x += 1
    if x > (len(row[y])-1):
        x -= len(row[y])

    try:
        if row[y][x] == "#":
            trees_hit1 += 1
    except IndexError:
        print("x="+str(x))
        print("y="+str(y))

x = 0
y = 0

#trees_hit2
while y < len(row)-1:
    y += 1

    x += 3
    if x > (len(row[y])-1):
        x -= len(row[y])

    try:
        if row[y][x] == "#":
            trees_hit2 += 1
    except IndexError:
        print("x="+str(x))
        print("y="+str(y))

x = 0
y = 0

#trees_hit3
while y < len(row)-1:
    y += 1

    x += 5
    if x > (len(row[y])-1):
        x -= len(row[y])

    try:
        if row[y][x] == "#":
            trees_hit3 += 1
    except IndexError:
        print("x="+str(x))
        print("y="+str(y))

x = 0
y = 0

#trees_hit4
while y < len(row)-1:
    y += 1

    x += 7
    if x > (len(row[y])-1):
        x -= len(row[y])

    try:
        if row[y][x] == "#":
            trees_hit4 += 1
    except IndexError:
        print("x="+str(x))
        print("y="+str(y))

x = 0
y = 0

#trees_hit5
while y < len(row)-1:
    y += 2

    x += 1
    if x > (len(row[y])-1):
        x -= len(row[y])

    try:
        if row[y][x] == "#":
            trees_hit5 += 1
    except IndexError:
        print("x="+str(x))
        print("y="+str(y))

print (trees_hit1*trees_hit2*trees_hit3*trees_hit4*trees_hit5)