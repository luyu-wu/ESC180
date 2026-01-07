def maximum_party_size(seats):
    most = 0
    for row in seats:
        counter = 0
        for i in row:
            if i == 0:
                counter += 1
            else:
                if counter > most:
                    most = counter
                counter = 0
        if counter > most:
            most = counter
    return most

seats = [[1,0,1,1,1],
[0,0,0,0,0],
[0,0,1,0,0]]
print(maximum_party_size(seats))
