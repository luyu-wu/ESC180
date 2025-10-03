def initialize():
    global a, b, c, cur, my_max
    #a = 438750932854830938457
    #b = 287492837491
    a = 100
    b = 50
    cur = 1
    my_max = 100000
    
def next_cur():
    global cur
    cur = (cur * a % b)
    return cur % my_max
    
def myrandom():
    return next_cur()/my_max
    
initialize()

if __name__ == '__main__':
    print(myrandom())
    print(myrandom())
