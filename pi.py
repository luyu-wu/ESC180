import numpy as np
import numpy.linalg as la

r = 1
N = 100000
x1 = np.random.rand(N,2)*2 - 1
in_cir = 0
for pos in x1:
    if la.norm(pos) < r:
        in_cir += 1

print(4*in_cir/N)

i = 0
in_cir = 0
while i < N:
    if la.norm(x1[i]) < r:
        in_cir += 1
    i += 1

print(4*in_cir/N)
