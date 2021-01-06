seats = open("input.txt", "r")

max_seat_id = 0
sid = 0 #seat id
row = 0
column = 0

# We'll basically treat these strings as binary numbers, 
# except we have B/F and R/L instead of 1s and 0s. So, 
# each index in the string is like the place value in a 
# binary number. If it's a "1", we increment by the 
# place value and divide by two to get the next place value.

for i in seats:
    placevalue = 64
    for j in range(7):
        if i[j] == "B":
            row += placevalue
        placevalue = placevalue/2
    
    placevalue = 4
    for k in range(7, 10):
        if i[k] == "R":
            column += placevalue
        placevalue = placevalue/2
    
    sid = (row*8)+column

    if sid > max_seat_id:
        max_seat_id = sid

    sid = 0
    row = 0
    column = 0


print(max_seat_id)
