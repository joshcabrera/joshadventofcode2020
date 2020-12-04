text = open("input.txt", "r") #open the file

trees_hit = 0 #count the trees hit

row = [] #we'll make a list of strings

x = 0 #these will be our coordinates 
y = 0 #down is up as far as y is concerned

for i in text: #fill our list of strings
    row.append(i.rstrip()) #take off the newline character

while y < len(row)-1: #once we go past the last row, we can stop
    y += 1 #go down (up) one
    x += 3 #go to the right three
    if x > (len(row[y])-1): #if we go past the right, we can wrap back
        x -= len(row[y])
    try:
        if row[y][x] == "#": #check for a rock
            trees_hit += 1
    except IndexError: #used this to troubleshoot going too far
        print("x="+str(x))
        print("y="+str(y))

print (trees_hit)