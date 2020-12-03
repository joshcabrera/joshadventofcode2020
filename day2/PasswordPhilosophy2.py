passwords = open("passwords.txt", "r") # open the file

count = 0 # we'll print our count at the end

for i in passwords: # go through each line in the file
    three_terms = i.split() # split the line into three parts

    indices = three_terms[0].split("-") # split the first part into two more parts

    # let's collect the positions that we'll check for the character
    firstpos = int(indices[0]) 
    secondpos = int(indices[-1])

    # if the character == the character at the first position but not the second, we'll count that as success
    if three_terms[1][0] == three_terms[2][firstpos-1] and not three_terms[1][0] == three_terms[2][secondpos-1]:
        count += 1
    # and now the inverse (these two are mutually exclusive)
    if three_terms[1][0] == three_terms[2][secondpos-1] and not three_terms[1][0] == three_terms[2][firstpos-1]:
        count += 1

print (count)