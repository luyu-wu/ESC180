# Problem 1
print("\nProblem 1")

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

# we decompose it by returning x*x
def power(x,n):
    if n == 1:
        return x
    else:
        return x*power(x,n-1)

print(power(2,3))

# Problem 2
print("\nProblem 2")

def times(a,b):
    if b==1:
        return a
    else:
        return a+times(a,b-1)
print(times(2,3))

# Problem 3
print("\nProblem 4")

arr = [0,0,1,0]
def lin_search(arr,search,ind):
    if arr[0] == search:
        return ind
    else:
        return lin_search(arr[1:],search,ind+1)
print(lin_search(arr,1,0))

# Problem 4
print("\nProblem 4")
def interleave(L1,L2):
    if len(L2) > 0:
        L1.insert(1+int(len(L1)-len(L2)),L2[0] )
        return interleave(L1,L2[1:])
    return L1            

print(interleave([1,1,1],[0,0,0]))

# Problem 5
print("\nProblem 5")
def reverse_rec(L):
    if len(L) >= 2:
        arr = [L[-1],L[0]]
        arr.insert(1,reverse_rec(L[1:-1]))
        return arr
    else:
        return L[0]

print(reverse_rec([1,2,3]))

# Problem 6
print("\nProblem 6")
# go from half the list and print in out print
def zigzag(L):
    if len(L) == 0:
        print('')
    else:
        print(L[len(L)//2], end = " ")
        L.pop(len(L)//2)
        zigzag(L)

zigzag([1,2,3,4,5])

# Problem 7
print("\nProblem 7")

def sublists(arr,elements):
    arr_shell = []
    temp_arr = []
    for i in arr:
        drop = False
        for a in elements:
             if i == a:
                drop = True
                break             
        if drop:
            arr_shell.append(temp_arr)
            temp_arr = []
        else:
            temp_arr.append(i)
    if len(temp_arr) > 0:
        arr_shell.append(temp_arr)
    return arr_shell
print(sublists([1, 2, 6, 4, 5, 3, 7],[3,6]))
                


