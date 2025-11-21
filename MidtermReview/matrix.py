def matrix_sum(A,B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "ERROR"

    C = []
    for r in range(len(A)):
        at = []
        for c in range(len(A[r])):
            at.append(B[r][c]+A[r][c])
        C.append(at)

    return C

print(matrix_sum([[5,0,0],[0,0,1]],[[1,2,2],[2,2,2]]))
