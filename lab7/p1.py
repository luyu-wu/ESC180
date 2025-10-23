import numpy as np

M_listoflists = [[1, -2, 3], [3, 10, 1], [1, 5, 3]]
M = np.array(M_listoflists)
print(M)


# Compute M*x for matrix M and vector x by using
# dot. To do that, we need to obtain arrays
# M and x
M = np.array([[1, -2, 3], [3, 10, 1], [1, 5, 3]])
x = np.array([75, 10, -11])
b = np.matmul(M, x)

print(M)


# To obtain a list of lists from the array M, we use .tolist()
M_listoflists = M.tolist()

print(M_listoflists)  # [[1, -2, 3], [3, 10, 1], [1, 5, 3]]


def print_matrix(M_lol):
    for i in M_lol:
        print(i)


print_matrix(M_listoflists)


def get_lead_ind(row):
    for i, v in zip(range(len(row)), row):
        if v != 0:
            return i
    return len(row) - 1


def get_row_to_swap(M, start_i):
    lead = get_lead_ind(M[start_i])
    for i in range(start_i, len(M)):
        if get_lead_ind(M[i]) < lead:
            return i
    return start_i


def add_rows_coefs(r1, c1, r2, c2):
    return c1 * r1 + c2 * r2


def eliminate(M, row_to_sub, best_lead_ind):
    # Make the row start w 0
    M[row_to_sub] = M[row_to_sub] / M[row_to_sub, best_lead_ind]
    row = M[row_to_sub]
    for i in range(row_to_sub + 1, len(M)):
        M[i] -= M[i, best_lead_ind] * row
    return M


def forward_step(M):
    cont = True
    while cont:
        cont = False
        for i in range(len(M) - 1):
            val = get_row_to_swap(M, i)

            if val != i:
                M[[i, val]] = M[[val, i]]
                cont = True
            M = eliminate(M, i, get_lead_ind(M[i]))
    return M


def backward_step(M):
    for ind in -np.arange(1, len(M)):
        lead = get_lead_ind(M[ind])
        for i in range(0, len(M) + ind):
            M[i] -= M[i, lead] * (M[ind] / M[ind, lead])
    return M


print("\n\nForward Stepping\n\n")
M = np.array([[0, 1, 0, 0], [0, 0, 2, 1], [1, 1, 0, 0]], dtype="float64")
print(M)
print(forward_step(M))
print(backward_step(M))


def solve(M, x):
    b = np.array([(M @ x)], dtype="float64").T
    mat = np.concatenate((M, b), axis=1)
    print(mat)
    mat = forward_step(mat)
    mat = backward_step(mat)
    sol = []
    for i in mat:
        sol.append(i[-1] / i[get_lead_ind(i)])
    print(sol)
    print(x)


print("\n\nSol\n\n")
M = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype="float64")
x = np.array([2, 0, 1], dtype="float64")
solve(M, x)
