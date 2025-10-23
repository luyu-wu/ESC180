

## PROBLEM 1

# Part A
def dict_to_str(d):
    ret = ""
    for key in d:
        ret+=str(key) + ", "+str(d[key])+"\n"
    return ret
print(dict_to_str({1:2, 5:6}))

# Part B
def dict_to_str_sorted(d):
    arr = list(d.keys())
    arr.sort()        
    ret = ""
    for key in arr:
        ret+=str(key) + ", "+str(d[key])+"\n"
    return ret

print(dict_to_str_sorted({1:2, 0:3, 10:5}))


## PROBLEM 2

def luckiest_kid(d):
    most = "No-one got candy"
    most_num = 0
    people = {}
    for house in d:
        for person in d[house]:
            people[person] = 0
            
    for house in d:
        for person in d[house]:
            people[person] += len(d[house][person])
            
    for person in people:
        if people[person] > most_num:
            most = person
            most_num = people[person]
    return most

halloween_haul = {
    "house1": {
        "Annie": ["snickers", "mars"],
        "Johnny": ["snickers"]
    },
    "house2": {
        "Annie": ["coffee crisp", "mars"],
        "Jackie": ["coffee crisp"]
    }
}
print(luckiest_kid(halloween_haul))

## PROBLEM 3
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

def is_sequence_complete(board,col,y_start,x_start,length,d_y,d_x):
    for i in range(length):
        if board[y_start+d_y*i][x_start+d_x*i] != col:
            return False
    if board[y_start-d_y][x_start-d_x] == col or board[y_start+d_y*length][x_start+d_x*length]==col:
        return False
    return True

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board

board = make_empty_board(9)
put_seq_on_board(board,1,1,1,1,3,"w")
print(board)
print(is_sequence_complete(board,"w",1,1,3,1,1))
print(is_sequence_complete(board,"w",1,1,4,1,1))
put_seq_on_board(board,1,1,1,1,4,"w")
print(is_sequence_complete(board,"w",1,1,3,1,1))

# Old Lab 8
'''
f = open("data2.txt")
text = f.read()

lines = text.lower().split("\n")

for (i,v) in zip(range(len(lines)),lines):
    if v.lower().find('lol') != -1:
        print("Line",i,": "+v)

words = open("text.txt", encoding="latin-1").read().lower().split()

def word_counts(words):
    d = {}
    for i in words:
        d[i] = 0
    for i in words:
        d[i] = d[i] + 1
    return d

def keyf(n):
    return n[1]
def sort_frequency(freq):
    return sorted(freq.items(),key=keyf,reverse=True)
print(sort_frequency(word_counts(words)))

pride = open("prejudice.txt", encoding="latin-1").read().lower().split()
print(sort_frequency(word_counts(pride))[:10])

def top10(L):
    L.sort()
    return L[:10]
'''
