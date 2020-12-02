
report = open("input.txt", "r") # open our file again

array = []

for i in report:
    array.append(int(i[:-1]))

report.close()

for j in array:
    for k in array:
        for l in array:
            if (j+k+l)==2020:
                print(j*k*l)