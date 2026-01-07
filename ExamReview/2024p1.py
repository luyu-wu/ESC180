def find_lonely_sock(socks):
    doubled = []
    for i in range(len(socks)):
        if socks[i] in socks[:i]:
            doubled.append(socks[i])
    for i in socks:
        if not (i in doubled):
            return i

print(find_lonely_sock(["red","blue","blue","green","red"]))
