over = False
next = 2
def isPrime(num):
    for i in range(1,num):
        if num % i == 0 and i != 1 and i != num:
            return False
    return True

def check_next_prime(num):
    global over,next
    if over:
        print("Game is over")
        return
        
    if num != next:
        print("Incorrect, game over")
        over = True
        return

    print("Correct")
    next += 1
    while not isPrime(next):
        next += 1
    return
check_next_prime(2) # print "Correct"
check_next_prime(3) # print "Correct"
check_next_prime(4) # print "Incorrect, game over"
check_next_prime(5) # print "Game is over"
