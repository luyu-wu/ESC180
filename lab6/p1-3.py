L = [["CIV", 92],
["180", 98],
["103", 99],
["194", 95]]

print(L[2][1])

def get_nums(L):
    new = []
    for i in L:
        new.append(i[1])
    return new

print(get_nums(L))

def lookup(L,num):
    for i in L:
        if i[1] == num:
            return i[0]
    return ""

print(lookup(L,99))
