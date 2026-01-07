import numpy as np

estimate = 4
num_p = 10
while np.abs((estimate/np.pi) - 1) > 0.01:
    num_p += 1
    points = np.random.random((num_p,2))
    amount = np.sum(np.linalg.norm(points,axis=1) < 1)
    estimate = 4*amount /  num_p

print(num_p)
