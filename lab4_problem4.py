
# Method 1
def gcd(n,m):
    gc = False
    for i in range(1,1+min((n,m))):
        if n % i == 0 and m % i == 0:
            gc = i
    return gc


print(gcd(5,15))
# Approach 2

def gcd_efficient(n,m):
    gc = 0
    top = min((n,m))   
    found = False
    while top > 0:
        if n % top == 0 and m % top == 0:
            return top
        top -= 1

print(gcd_efficient(5,15))
