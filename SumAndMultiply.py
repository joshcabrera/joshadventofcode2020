report = open("input.txt", "r") # let's open our file

array = [] # we'll need a list to store our values

for i in report: # go through every line in the input file
    # first, we slice off the end of each string because
    # we don't want the newline character when we turn it
    # into an integer. we'll need integers because we'll
    # be doing math with each item in our list
    array.append(int(i[:-1]))

report.close() # close the file because we have good manners

# now we go through each item in the list and add it to
# every item in the list. this way will print the solution
# twice because we go through every loop even if success is found
for j in array:
    for k in array:
        if (j+k)==2020:
            print(j*k)