import numpy as np
def find_pi(N):
    sum = 0
    for i in range(N):
        sum += ((-1)**i)/(2*i+1)

    return sum*4

def agree(n1,n2):
    a = 0
    while n1//1 == n2//1:
        a += 1
        n1 = (n1%1) * 10
        n2 = (n2%1) * 10
    return a

print(find_pi(119))
print(find_pi(1688))

def find_min(num):
    pi = np.pi
    sum = 0
    count = 0
    while agree(sum*4,pi) < num:
        sum += ((-1)**count)/(2*count+1)
        count += 1
    return count

print(find_min(4))
print("For N=1000",agree(find_pi(1000),np.pi))
print("For N=5000",agree(find_pi(5000),np.pi))
print("For N=10000",agree(find_pi(10000),np.pi))
print("For N=50000",agree(find_pi(50000),np.pi))
