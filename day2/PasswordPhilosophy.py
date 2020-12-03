passwords = open("passwords.txt", "r") # open the file

count = 0 # we'll print our count at the end

for i in passwords: # go through each line in the file

    three_terms = i.split() # split the line into three parts

    ranges = three_terms[0].split("-") # split the first part into two more parts
    
    # now the first part is the lower limit; the string must have at least that
    # many occurrences. the second part is the maximum
    llimit = int(ranges[0]) 
    ulimit = int(ranges[-1])

    # now we use the count function of the string and the result must be
    # greater than or equal to the lower limit and less than or equal to the
    # upper limit. 
    if llimit <= three_terms[2].count(three_terms[1][0]) <= ulimit:
        count += 1

passwords.close() # close the file to stay on Santa's nice list

print (count) # result!