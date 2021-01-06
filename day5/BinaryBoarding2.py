seats = open("input.txt", "r")

max_seat_id = 0
sid = 0 #seat id
row = 0
column = 0

seat_ids = [] # let's make a list of all our seat ids

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

    seat_ids.append(sid)

    sid = 0
    row = 0
    column = 0

seat_ids.sort() # now let's sort it

# now we go through the list and if a seat number+1 isn't the 
# same as the next on the list, we know there's a seat number
# missing
for l in range(len(seat_ids)):
    if seat_ids[l]+1 != seat_ids[l+1]:
        print (seat_ids[l])
# this will produce an outofbounds error but that's okay
