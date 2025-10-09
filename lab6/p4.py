def E(x0, x1, x2, w01, w02, w12):
    term1 = x0 * x1 * w01
    term2 = x0 * x2 * w02
    term3 = x1 * x2 * w12
    return -(term1 + term2 + term3)
    

def print_all_energies(w01, w02, w12):
    for x0 in [-1, 1]:
        for x1 in [-1, 1]:
            for x2 in [-1, 1]:
                print("x: (", x0, x1, x2, ")", "E:",
                E(x0, x1, x2, w01, w02, w12))

if __name__ == '__main__':
    w01,w02,w12 = 2,-1,1
    print("\nInitial Energy")
    print_all_energies(w01, w02, w12)


    # Part A: If x*x1*w01 > 0 then term1 will be positive
    # meaning the returned value (which becomes negative)
    # will decrease

    # Part B:
    # The product of x0*x1 in this case is < 0 so the energy
    # will be increased when w_0 is increased
    print("\nPart B\n")
    x = [-1,1,1]
    if x[0]*x[1] > 0:
        w01 += 0.1
    else:
        w01 -= 0.1
    if x[0]*x[2] > 0:
        w02+=0.1
    else:
        w02-=0.1
    if x[1]*x[2] > 0:
        w12 += 0.1
    else:
        w12-=0.1
    print(w01,w02,w12)
    print(print_all_energies(w01,w02,w12))
    print("Energy in",x,"has decreased")




    # Part C & E
    w01,w02,w12 = 2,-1,1

    print("\nPart C\n")
    
    def store(x,weights): # The memory and current weights
        for i in range(6):
            if x[0]*x[1] > 0:
                weights[0] += 0.1
            else:
                weights[0] -= 0.1
            if x[0]*x[2] > 0:
                weights[1]+=0.1
            else:
                weights[1]-=0.1
            if x[1]*x[2] > 0:
                weights[2] += 0.1
            else:
                weights[2]-=0.1
        return weights

    # Part D, F
    print("\nPart D\n")
    (w01,w02,w12) = store(x,[w01,w02,w12])
    print(print_all_energies(w01,w02,w12))

